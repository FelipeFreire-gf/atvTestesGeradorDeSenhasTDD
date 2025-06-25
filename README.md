# AtividadesTestes# Gerador de Senhas com TDD em Python

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Um aplicativo de desktop simples e robusto para gerar senhas seguras, construído com Python e Tkinter. Este projeto foi desenvolvido como um exercício prático para aplicar a metodologia de **Desenvolvimento Guiado por Testes (TDD)**, demonstrando como construir uma funcionalidade de forma incremental e segura.

## 🚀 Funcionalidades

*   **Interface Gráfica Intuitiva**: Interface limpa e fácil de usar construída com Tkinter.
*   **Comprimento Personalizável**: Escolha o tamanho da senha, de 4 a 64 caracteres.
*   **Critérios de Complexidade**: Selecione se deseja incluir:
    *   Letras Maiúsculas (A-Z)
    *   Letras Minúsculas (a-z)
    *   Números (0-9)
    *   Símbolos (`!@#$%^&*()-_=+`)
*   **Garantia de Inclusão**: O sistema garante que pelo menos um caractere de cada categoria selecionada estará presente na senha final.
*   **Copiar para a Área de Transferência**: Botão para copiar a senha gerada com um único clique.
*   **Cobertura de Testes**: Lógica do gerador 100% coberta por testes unitários.

## 🛠️ Tecnologias Utilizadas

*   **Python 3**
*   **Tkinter**: Para a interface gráfica (biblioteca padrão do Python).
*   **unittest**: Para os testes unitários (biblioteca padrão do Python).

## ⚙️ Como Executar a Aplicação

1.  **Clone o repositório:**
    ```bash
    git clone <https://github.com/FelipeFreire-gf/AtividadesTestes>
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd senhas
    ```
3.  **Execute o arquivo principal:**
    ```bash
    python geraSenha.py
    ```

## 🧪 Rodando os Testes

O coração deste projeto é a sua suíte de testes, que valida toda a lógica de negócios do gerador de senhas. Para executar os testes, utilize o seguinte comando no terminal, a partir da pasta raiz do projeto:

```bash
python -m unittest test_geraSenha.py
```

Você verá a saída indicando que todos os testes passaram com sucesso.

## 📂 Estrutura do Projeto

```
senhas/
├── geraSenha.py             # Arquivo principal com a GUI (Tkinter) e a lógica final.
├── password_logic.py        # Apenas a lógica do gerador, construída durante o TDD.
├── test_geraSenha.py        # Suíte de testes final e polida.
└── test_password_logic.py   # Testes criados passo a passo durante a simulação TDD.
```

## 🧠 A Jornada com TDD

Este projeto foi desenvolvido seguindo o ciclo **Red-Green-Refactor** do TDD. Os arquivos `password_logic.py` e `test_password_logic.py` são um registro dessa jornada, onde cada funcionalidade foi implementada da seguinte forma:

1.  **🔴 RED**: Primeiro, um teste era escrito para uma funcionalidade que ainda não existia. Naturalmente, este teste falhava.
2.  **🟢 GREEN**: Em seguida, o código mais simples possível era escrito para fazer o teste passar.
3.  **🔵 REFACTOR**: Com a segurança do teste, o código era refatorado para melhorar sua qualidade, clareza e eficiência, sem alterar seu comportamento.

Este processo foi repetido para cada pequena regra de negócio (tamanho, inclusão de maiúsculas, minúsculas, números e símbolos), garantindo um código final robusto e confiável.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
