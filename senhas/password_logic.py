# password_logic.py
import string
import random

class PasswordGenerator:
    def __init__(self, tamanho, incluir_maiusculas=False, incluir_minusculas=False, incluir_numeros=False, incluir_simbolos=False):
        if not isinstance(tamanho, int) or tamanho <= 0:
            raise ValueError("O tamanho deve ser um número inteiro positivo.")
        self.tamanho = tamanho
        self.incluir_maiusculas = incluir_maiusculas
        self.incluir_minusculas = incluir_minusculas
        self.incluir_numeros = incluir_numeros
        self.incluir_simbolos = incluir_simbolos

    def gerar(self):
        if not any([self.incluir_maiusculas, self.incluir_minusculas, self.incluir_numeros, self.incluir_simbolos]):
            raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")

        pool_de_caracteres = ""
        senha_garantida = []

        if self.incluir_maiusculas:
            pool_de_caracteres += string.ascii_uppercase
            senha_garantida.append(random.choice(string.ascii_uppercase))
        if self.incluir_minusculas:
            pool_de_caracteres += string.ascii_lowercase
            senha_garantida.append(random.choice(string.ascii_lowercase))
        if self.incluir_numeros:
            pool_de_caracteres += string.digits
            senha_garantida.append(random.choice(string.digits))
        if self.incluir_simbolos:
            simbolos = "!@#$%^&*()-_=+"
            pool_de_caracteres += simbolos
            senha_garantida.append(random.choice(simbolos))
    
        tamanho_restante = self.tamanho - len(senha_garantida)
        senha_restante = random.choices(pool_de_caracteres, k=tamanho_restante)
        senha_final_lista = senha_garantida + senha_restante
        random.shuffle(senha_final_lista)
        return "".join(senha_final_lista)
