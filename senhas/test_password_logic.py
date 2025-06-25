# test_password_logic.py
import unittest
import string
from password_logic import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    
    def test_gera_senha_com_tamanho_correto(self):
        tamanho_desejado = 10
        gerador = PasswordGenerator(tamanho=tamanho_desejado, incluir_maiusculas=True, incluir_minusculas=True)
        senha = gerador.gerar()
        self.assertEqual(len(senha), tamanho_desejado)

    def test_deve_incluir_maiuscula_se_solicitado(self):
        gerador = PasswordGenerator(tamanho=12, incluir_maiusculas=True, incluir_minusculas=False)
        senha = gerador.gerar()
        tem_maiuscula = any(c.isupper() for c in senha)
        self.assertTrue(tem_maiuscula, "A senha deveria conter ao menos uma letra maiúscula.")

    def test_deve_incluir_minuscula_se_solicitado(self):
        gerador = PasswordGenerator(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True)
        senha = gerador.gerar()
        tem_minuscula = any(c.islower() for c in senha)
        self.assertTrue(tem_minuscula, "A senha deveria conter ao menos uma letra minúscula.")

    def test_deve_incluir_numero_se_solicitado(self):
        gerador = PasswordGenerator(tamanho=12, incluir_numeros=True, incluir_simbolos=True, incluir_maiusculas=False, incluir_minusculas=False)
        senha = gerador.gerar()
        tem_numero = any(c.isdigit() for c in senha)
        self.assertTrue(tem_numero, "A senha deveria conter ao menos um número.")

    def test_deve_incluir_simbolo_se_solicitado(self):
        simbolos_definidos = "!@#$%^&*()-_=+"
        gerador = PasswordGenerator(tamanho=12, incluir_maiusculas=True, incluir_simbolos=True)
        senha = gerador.gerar()
        tem_simbolo = any(c in simbolos_definidos for c in senha)
        self.assertTrue(tem_simbolo, "A senha deveria conter ao menos um símbolo.")

if __name__ == '__main__':
    unittest.main()
