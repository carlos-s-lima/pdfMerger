# 🔗 PDF Merger CLI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-Bash-orange?style=flat&logo=gnu-bash)

Ferramenta de linha de comando (CLI) em Python para mesclar múltiplos arquivos PDF de forma segura, previsível e reprodutível. Projetada com princípios de Programação Orientada a Objetos para facilitar manutenção e futura evolução (ex.: GUI).

---

## Principais funcionalidades

- Mesclagem de múltiplos PDFs na ordem informada.
- Contagem de páginas por arquivo e total esperado.
- Prevenção de sobrescrita com versionamento automático do arquivo de saída (ex.: merged_cli.pdf → merged_cli_1.pdf).
- Criação automática do diretório de saída, quando ausente.
- Saídas claras no terminal: progresso, sucessos e erros.
- Arquitetura modular e testável (classes separadas para responsabilidades).

---

## Arquitetura (visão geral)

- src/pdfmerger/main.py
  - Orquestra a execução: parse de args, validação, soma de páginas, execução da mesclagem e código de saída.
- src/pdfmerger/cli_utils.py
  - Tratamento de argumentos (argparse) e lógica de obtenção de caminho único para saída (get_unique_output_path).
- src/pdfmerger/files.py
  - Classe PdfFile: valida existência, lê arquivo via pypdf e expõe page_count e get_reader().
- src/pdfmerger/merger.py
  - Classe Merger: mantém lista de PdfFile, adiciona/remove arquivos e realiza a escrita final via pypdf.PdfWriter.
- src/pdfmerger/status.py
  - Enum Status para controlar estados: WAITING, PROCESSING, SUCCESS, ERROR.

Separação de responsabilidades:
- PdfFile cuida de validação/leitura do PDF.
- Merger cuida apenas do processo de mesclagem.
- Main lida com interação com o usuário (terminal) e fluxo de execução.

---

## Requisitos

- Python 3.8+
- Dependência: pypdf

Instalar com pip:
```bash
pip install pypdf
```

Recomendado: usar Poetry ou venv para isolar dependências.

---

## Instalação (exemplos)

Com Poetry:
```bash
poetry install
```

Com venv (Windows):
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install pypdf
```

---

## Uso (CLI)

Sintaxe:
```bash
# Exemplo geral (quando executando o script main.py do diretório do projeto)
python main.py arquivo1.pdf arquivo2.pdf -o output/saida.pdf

# Com Poetry
poetry run python main.py arquivo1.pdf arquivo2.pdf -o output/saida.pdf
```

Comportamento padrão:
- Se `-o/--output` não for fornecido, o arquivo alvo será `output/merged_cli.pdf`.
- Se `output/` não existir, será criado automaticamente.
- Se `merged_cli.pdf` já existir, será criado `merged_cli_1.pdf`, `merged_cli_2.pdf`, etc.

Exemplo (Windows):
```powershell
python main.py C:\docs\a.pdf C:\docs\b.pdf -o C:\docs\output\final.pdf
```

Saída no terminal:
- Mensagens [OK] para arquivos processados com contagem de páginas.
- Avisos/erros para arquivos não encontrados ou com leitura inválida.
- Resumo final com total de arquivos, páginas esperadas e caminho do arquivo gerado.
- Código de saída não-zero em caso de falha (sys.exit(1)).

---

## Erros e tratamento

- Arquivos inexistentes → mensagem de erro e término com código 1.
- Falha na leitura de PDF → aviso (arquivo ignorado ou processo interrompido conforme o caso).
- Falha durante mesclagem → status ERROR e mensagem com motivo; saída com código 1.

---

## Boas práticas e notas de implementação

- Os objetos PdfFile armazenam um PdfReader apenas quando necessário (lazy).
- Merger usa PdfWriter para anexar leitores e escrever o arquivo final; sempre encerra o writer no finally.
- Mantém estado via Status enum para facilitar integração com interfaces futuras.

---

## Testes e desenvolvimento

- Arquitetura modular facilita criação de testes unitários por componente (PdfFile, Merger, cli_utils).
- Sugestão: usar pytest e monkeypatch para simular arquivos e comportamento de pypdf.

---

## Contribuição

- Abrir issue para bugs ou sugestões.
- Enviar PR com descrição clara e testes (quando aplicável).
- Seguir estilo de código do projeto e manter compatibilidade com Python 3.8+.

---

## Licença

Adicionar licença do projeto conforme desejado (por exemplo MIT). 

<!-- ...existing code... -->