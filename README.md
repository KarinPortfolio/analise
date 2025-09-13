# 💫 Análise de Signos - Relacionamentos Astrológicos

Uma aplicação web Flask divertida que analisa a relação entre signos do zodíaco e a duração de relacionamentos. 

> **Nota:** Este é um projeto apenas para entretenimento, sem base científica! 😉

## 🌟 Sobre o Projeto

Esta aplicação permite que usuários insiram dados sobre seus relacionamentos (signos dos parceiros e duração) e visualizem análises estatísticas interessantes sobre as combinações de signos mais e menos duradouras.

### Funcionalidades

- 📝 **Formulário de entrada**: Colete dados sobre signos e duração do relacionamento
- 📊 **Análises estatísticas**: Visualize qual combinação de signos tem relacionamentos mais duradouros
- 📈 **Gráficos interativos**: Visualização gráfica dos dados coletados
- 🗄️ **Persistência de dados**: Armazenamento em banco de dados PostgreSQL
- ✅ **Validação de dados**: Validação robusta de entrada de dados

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: PostgreSQL com SQLAlchemy
- **Frontend**: HTML, CSS (templates Jinja2)
- **Visualização**: Matplotlib
- **Deploy**: Configurado para Render.com
- **Testes**: unittest

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8+
- PostgreSQL (ou configurar variáveis de ambiente para outro banco)

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd analise
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto:
```env
FLASK_SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

6. Execute a aplicação:
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 📁 Estrutura do Projeto

```
analise/
├── app.py              # Aplicação principal Flask
├── chave.py           # Configurações de chave (se aplicável)
├── requirements.txt   # Dependências do projeto
├── test_app.py       # Testes unitários
├── README.md         # Este arquivo
└── templates/        # Templates HTML
    ├── base.html     # Template base
    ├── form.html     # Formulário de entrada
    └── analise.html  # Página de análise
```

## 🧪 Executando os Testes

Para executar os testes unitários:

```bash
python test_app.py
```

Os testes cobrem:
- ✅ Validação de signos válidos
- ✅ Validação de signos inválidos
- ✅ Validação de durações válidas e inválidas
- ✅ Tratamento de casos extremos

## 🌐 Deploy

Este projeto está configurado para deploy no **Render.com**:

1. A aplicação usa `gunicorn` como servidor WSGI
2. O banco de dados PostgreSQL é configurado via variável `DATABASE_URL`
3. As tabelas são criadas automaticamente na inicialização

### Variáveis de Ambiente Necessárias

- `FLASK_SECRET_KEY`: Chave secreta para sessions Flask
- `DATABASE_URL`: URL de conexão com o banco PostgreSQL

## 📊 Como Usar

1. **Acesse a página inicial** e preencha o formulário com:
   - Seu signo
   - Signo do(a) parceiro(a)
   - Duração do relacionamento em dias

2. **Visualize as análises** na página de resultados:
   - Combinação de signos com maior duração total
   - Combinação de signos com menor duração total
   - Média geral de duração
   - Gráfico de linha mostrando todas as combinações

## 🎯 Validações Implementadas

- **Signos**: Apenas os 12 signos do zodíaco são aceitos
- **Duração**: Deve ser um número inteiro entre 1 e 36.525 dias (100 anos)
- **Duplicatas**: Combinações de signos são normalizadas (Áries + Touro = Touro + Áries)

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é apenas para fins educacionais e de entretenimento.

## 🔮 Signos Suportados

- ♈ Áries
- ♉ Touro
- ♊ Gêmeos
- ♋ Câncer
- ♌ Leão
- ♍ Virgem
- ♎ Libra
- ♏ Escorpião
- ♐ Sagitário
- ♑ Capricórnio
- ♒ Aquário
- ♓ Peixes

---

**Lembre-se**: Este é um projeto para diversão! As estrelas podem influenciar muitas coisas, mas o que realmente importa nos relacionamentos são o carinho, respeito e compreensão mútua. 💕