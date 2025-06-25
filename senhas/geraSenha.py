import tkinter as tk
from tkinter import ttk, messagebox
import string
import random


class PasswordGenerator:
    """
    Gera senhas aleatórias com base em critérios definidos pelo usuário.
    """
    def __init__(self, tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
        if not isinstance(tamanho, int) or tamanho <= 0:
            raise ValueError("O tamanho deve ser um número inteiro positivo.")
        
        self.tamanho = tamanho
        self.incluir_maiusculas = incluir_maiusculas
        self.incluir_minusculas = incluir_minusculas
        self.incluir_numeros = incluir_numeros
        self.incluir_simbolos = incluir_simbolos

    def gerar(self):
        """
        Gera a senha com base nos critérios fornecidos no construtor.
        - Garante que ao menos um caractere de cada categoria selecionada esteja presente.
        - Lança uma exceção se nenhuma categoria de caractere for selecionada.
        """
        if not any([self.incluir_maiusculas, self.incluir_minusculas, self.incluir_numeros, self.incluir_simbolos]):
            raise ValueError("Pelo menos um critério (maiúsculas, minúsculas, números, símbolos) deve ser selecionado.")

        # Lista para garantir ao menos um caractere de cada tipo escolhido
        senha_garantida = []
        # String com todos os caracteres possíveis para o restante da senha
        pool_de_caracteres = ""

        # Monta os pools de caracteres e garante um de cada tipo selecionado
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
        
        # O número de caracteres restantes a serem preenchidos aleatoriamente
        tamanho_restante = self.tamanho - len(senha_garantida)
        
        # Preenche o restante da senha com caracteres aleatórios do pool completo
        senha_restante = random.choices(pool_de_caracteres, k=tamanho_restante)
        
        # Junta a parte garantida com a parte restante e embaralha
        senha_final_lista = senha_garantida + senha_restante
        random.shuffle(senha_final_lista)
        
        # Converte a lista de caracteres em uma string e a retorna
        return "".join(senha_final_lista)

# Parte 2: A Interface Gráfica com Tkinter 
class App:
    """
    Interface gráfica para o Gerador de Senhas.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')

        self.tamanho_var = tk.IntVar(value=12)
        self.maiusculas_var = tk.BooleanVar(value=True)
        self.minusculas_var = tk.BooleanVar(value=True)
        self.numeros_var = tk.BooleanVar(value=True)
        self.simbolos_var = tk.BooleanVar(value=True)
        self.senha_gerada_var = tk.StringVar()

        self.criar_widgets()

    def criar_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill="both")

        ttk.Label(main_frame, text="Configurações da Senha", font=("Helvetica", 16, "bold")).pack(pady=(0, 20))

        options_frame = ttk.Frame(main_frame)
        options_frame.pack(fill="x", pady=5)

        ttk.Label(options_frame, text="Tamanho da Senha:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tamanho_spinbox = ttk.Spinbox(options_frame, from_=4, to=64, textvariable=self.tamanho_var, width=5)
        tamanho_spinbox.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        ttk.Checkbutton(options_frame, text="Incluir Letras Maiúsculas (A-Z)", variable=self.maiusculas_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        ttk.Checkbutton(options_frame, text="Incluir Letras Minúsculas (a-z)", variable=self.minusculas_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        ttk.Checkbutton(options_frame, text="Incluir Números (0-9)", variable=self.numeros_var).grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        ttk.Checkbutton(options_frame, text="Incluir Símbolos (!@#$...)", variable=self.simbolos_var).grid(row=4, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        gerar_button = ttk.Button(main_frame, text="Gerar Senha", command=self.gerar_senha_action, style="Accent.TButton")
        gerar_button.pack(pady=20, ipadx=10, ipady=5)

        self.style.configure("Accent.TButton", font=("Helvetica", 12, "bold"))

        resultado_frame = ttk.LabelFrame(main_frame, text="Senha Gerada", padding="10")
        resultado_frame.pack(fill="x", pady=10)

        senha_entry = ttk.Entry(resultado_frame, textvariable=self.senha_gerada_var, font=("Courier", 14), state="readonly")
        senha_entry.pack(fill="x", expand=True, ipady=5)
        
        copiar_button = ttk.Button(resultado_frame, text="Copiar", command=self.copiar_para_clipboard)
        copiar_button.pack(pady=(10, 0))

    def gerar_senha_action(self):
        """
        Função chamada pelo botão para gerar e exibir a senha.
        """
        try:
            # 1. Coleta os valores da interface
            tamanho = self.tamanho_var.get()
            incluir_maiusculas = self.maiusculas_var.get()
            incluir_minusculas = self.minusculas_var.get()
            incluir_numeros = self.numeros_var.get()
            incluir_simbolos = self.simbolos_var.get()

            # 2. Cria uma instância do gerador
            gerador = PasswordGenerator(
                tamanho=tamanho,
                incluir_maiusculas=incluir_maiusculas,
                incluir_minusculas=incluir_minusculas,
                incluir_numeros=incluir_numeros,
                incluir_simbolos=incluir_simbolos
            )
            
            # 3. Chama o método para gerar a senha
            senha = gerador.gerar()

            # 4. Exibe a senha na interface
            self.senha_gerada_var.set(senha)

        except ValueError as e:

            messagebox.showerror("Erro de Validação", str(e))
            self.senha_gerada_var.set("")
        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")
            self.senha_gerada_var.set("")

    def copiar_para_clipboard(self):
        """
        Copia a senha gerada para a área de transferência.
        """
        senha = self.senha_gerada_var.get()
        if senha:
            self.root.clipboard_clear()
            self.root.clipboard_append(senha)
            messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()