import unittest
from app import validar_dados, SIGNOS_VALIDOS 

class TestValidacao(unittest.TestCase):

    def test_validos(self):
        self.assertEqual(validar_dados("Áries", "Touro", "12"), (True, ""))
        self.assertEqual(validar_dados("Peixes", "Libra", "1"), (True, ""))

        self.assertEqual(validar_dados("Câncer", "Capricórnio", "36525"), (True, ""))



    def test_invalidos_signo(self):

        self.assertEqual(validar_dados("X", "Touro", "12")[0], False) 

        self.assertEqual(validar_dados("X", "Touro", "12")[1], "Signos inválidos.") 

        self.assertEqual(validar_dados("Áries", "Y", "12")[0], False)
        self.assertEqual(validar_dados("Áries", "Y", "12")[1], "Signos inválidos.") 
    

    def test_invalidos_duracao(self):
        self.assertEqual(validar_dados("Áries", "Touro", "0")[0], False)
        self.assertEqual(validar_dados("Áries", "Touro", "0")[1], "Duração deve ser entre 1 e 36525 dias.") # Verifica a mensagem específica

        self.assertEqual(validar_dados("Áries", "Touro", "-5")[0], False)
        self.assertEqual(validar_dados("Áries", "Touro", "-5")[1], "Duração deve ser entre 1 e 36525 dias.")

        self.assertEqual(validar_dados("Áries", "Touro", "abc")[0], False)
        self.assertEqual(validar_dados("Áries", "Touro", "abc")[1], "Duração deve ser um número inteiro.")
        

        self.assertEqual(validar_dados("Áries", "Touro", "36526")[0], False)
        self.assertEqual(validar_dados("Áries", "Touro", "36526")[1], "Duração deve ser entre 1 e 36525 dias.")


if __name__ == '__main__':
    unittest.main()
