# 🔗 PDF Merger CLI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI%20(argparse)-brightgreen)

Este projeto é uma ferramenta de linha de comando (CLI) desenvolvida em Python para mesclar múltiplos arquivos PDF de forma segura e ordenada. A arquitetura segue o paradigma de Programação Orientada a Objetos (POO), garantindo a separação de responsabilidades e preparando a base para uma futura interface gráfica (GUI).

---

## ✨ Funcionalidades

A aplicação oferece as seguintes funcionalidades principais via linha de comando:

* **Seleção Flexível:** Aceita um ou mais caminhos de arquivos PDF como entrada (`argparse` com `nargs='+'`). Os caminhos podem ser absolutos (de qualquer lugar do sistema) ou relativos.
* **Mesclagem Ordenada:** Os arquivos são mesclados na ordem exata em que são fornecidos como argumentos na CLI.
* **Contagem de Páginas:** Exibe o número de páginas de cada arquivo de entrada e o total esperado após a mesclagem.
* **Prevenção de Sobrescrita:** Implementa **Versionamento Automático** na saída (ex: `merged_cli_1.pdf`, `merged_cli_2.pdf`) para garantir que nenhum arquivo existente seja perdido acidentalmente.
* **Arquitetura POO:** A lógica de negócio está encapsulada nas classes (`Merger`, `PdfFile`, `Status`), facilitando a transição para uma GUI no futuro.

---

## ⚙️ Instalação e Dependências

A única dependência externa necessária para a execução do programa é a biblioteca `pypdf`.

### Requisitos

* **Python:** Versão 3.8+
* **pypdf:** Biblioteca para manipulação de PDFs.

### Setup (Recomendado: Poetry)

Para desenvolvedores, recomenda-se o uso do [Poetry](https://python-poetry.org/) para gerenciar o ambiente:

1.  **Clone o repositório:**
    ```bash
    git clone [SEU_LINK_DO_REPOSITORIO]
    cd [pasta-do-projeto]
    ```

2.  **Instale as dependências:**
    ```bash
    poetry install
    ```

### Setup (Alternativo: Pip/Venv)

Para usuários finais que preferem ambientes virtuais padrão (`venv`):

1.  **Crie e Ative o ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
    ```
2.  **Instale a dependência:**
    ```bash
    pip install pypdf
    ```

---

## 🚀 Uso da Aplicação (CLI)

A aplicação é executada através do script `main.py`.

### Sintaxe Básica

```bash
# Se estiver usando Poetry:
poetry run python main.py [ARQUIVO_1] [ARQUIVO_2] ... [ARQUIVO_N] [-o NOME_DE_SAIDA]

# Se estiver usando venv/Pip ativo:
python main.py [ARQUIVO_1] [ARQUIVO_2] ... [ARQUIVO_N] [-o NOME_DE_SAIDA]