from flask import Flask, render_template, request, redirect, url_for, flash
import matplotlib.pyplot as plt
from collections import defaultdict
import io
import base64
import os
from dotenv import load_dotenv

# Importa Flask-SQLAlchemy em vez de Flask-MySQLdb
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Configurações do banco de dados para PostgreSQL usando SQLALCHEMY_DATABASE_URI
# O Render.com, para seus bancos de dados PostgreSQL gerenciados,
# geralmente fornece uma variável de ambiente chamada DATABASE_URL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Desativa o rastreamento de modificações de objetos SQLAlchemy,
# o que economiza memória e é recomendado para a maioria dos casos.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

# Define o modelo do banco de dados (corresponde à sua tabela 'relacoes')
# Este é um passo crucial para o SQLAlchemy
class Relacao(db.Model):
    __tablename__ = 'relacoes' # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True) # SERIAL no PostgreSQL, mapeado para Integer com primary_key=True
    signo1 = db.Column(db.String(20), nullable=False)
    signo2 = db.Column(db.String(20), nullable=False)
    duracao_dias = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Relacao {self.signo1} + {self.signo2}: {self.duracao_dias} dias>"

SIGNOS_VALIDOS = ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra",
                  "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html', signos=SIGNOS_VALIDOS)

def validar_dados(signo1, signo2, duracao):
    if signo1 not in SIGNOS_VALIDOS or signo2 not in SIGNOS_VALIDOS:
        return False, "Signos inválidos."
    try:
        duracao = int(duracao)
        if duracao < 1 or duracao > 36525:
            return False, "Duração deve ser entre 1 e 36525 dias."
    except ValueError:
        return False, "Duração deve ser um número inteiro."
    return True, ""

@app.route('/submit', methods=['POST'])
def submit():
    signo1 = request.form.get('signo1')
    signo2 = request.form.get('signo2')
    duracao = request.form.get('duracao')

    valido, msg = validar_dados(signo1, signo2, duracao)
    if not valido:
        flash(msg)
        return redirect(url_for('index'))

    signos_sorted = sorted([signo1, signo2])
    
    # Cria uma nova instância do modelo Relacao
    new_relacao = Relacao(
        signo1=signos_sorted[0],
        signo2=signos_sorted[1],
        duracao_dias=int(duracao)
    )

    try:
        # Adiciona a nova relação à sessão do banco de dados
        db.session.add(new_relacao)
        # Confirma as mudanças no banco de dados
        db.session.commit()
    except Exception as e:
        # Em caso de erro, desfaz a operação
        db.session.rollback()
        flash("Erro ao salvar no banco: " + str(e))
        return redirect(url_for('index'))

    flash("Dados salvos com sucesso!")
    return redirect(url_for('index'))

@app.route('/analise')
def analise():
    # Consulta todos os dados da tabela 'relacoes'
    # Os dados virão como objetos Relacao
    dados_obj = Relacao.query.all()

    if not dados_obj:
        return render_template('analise.html', dados=None)

    agrupado = defaultdict(list)
    # Iterar sobre os objetos e acessar seus atributos
    for relacao in dados_obj:
        chave = " + ".join(sorted([relacao.signo1, relacao.signo2]))
        agrupado.setdefault(chave, []).append(relacao.duracao_dias)

    soma_por_combinacao = {k: sum(v) for k, v in agrupado.items()}

    maior = max(soma_por_combinacao.items(), key=lambda item: item[1])
    menor = min(soma_por_combinacao.items(), key=lambda item: item[1])

    todas_duracoes = [dur for v in agrupado.values() for dur in v]
    media_geral = sum(todas_duracoes) / len(todas_duracoes)

    labels = list(soma_por_combinacao.keys())
    sizes = list(soma_por_combinacao.values())

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(labels, sizes, marker='o', linestyle='-')
    ax.set_xlabel('Combinação de Signos')
    ax.set_ylabel('Soma Total da Duração (dias)')
    plt.title('Soma Total da Duração por Combinação de Signos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    grafico_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)

    return render_template(
        'analise.html',
        maior_combinacao=maior[0],
        maior_duracao=maior[1],
        menor_combinacao=menor[0],
        menor_duracao=menor[1],
        media_geral_formatada=f"{media_geral:.2f}",
        grafico_url=grafico_url,
        dados=dados_obj # Ainda passando os dados_obj caso o template precise deles
    )

# Função para criar a tabela no banco de dados usando SQLAlchemy
def criar_tabela():
    with app.app_context(): # Garante que estamos no contexto da aplicação
        try:
            # Cria todas as tabelas definidas como db.Model, se não existirem
            db.create_all()
            print("--- SUCESSO: Tabela 'relacoes' criada ou já existente. ---")
        except Exception as e:
            print(f"--- ERRO CRÍTICO NA CRIAÇÃO DA TABELA: {e} ---")

if __name__ == '__main__':
    with app.app_context():
        print("Tentando criar a tabela no banco de dados...")
        criar_tabela()
        print("Verificação de criação de tabela concluída.")
    app.run(debug=True)