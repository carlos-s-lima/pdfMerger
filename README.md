# Mesclador de PDFs em Python

## Logo da Linguagem

![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Projeto de Mesclagem de PDFs em Python

Este documento apresenta a estrutura e as funcionalidades de um projeto em Python voltado para a mesclagem (combinação) de múltiplos arquivos PDF em um único documento. A arquitetura atual é simples e visa a modularidade, facilitando futuras expansões.

---

### Funcionalidades Atuais

O projeto é composto por três módulos principais: status.py, merger.py e main.py.

#### 1. Módulo status.py

O status.py utiliza a classe Enum do Python para definir um conjunto de estados bem definidos para o processo de mesclagem:

* WAITING: Estado inicial, aguardando a execução.
* PROCESSING: A mesclagem está em andamento.
* SUCCESS: Mesclagem concluída com sucesso.
* ERROR: Um erro ocorreu durante a mesclagem.

A vantagem é que isso garante que o estado da operação seja sempre uma das opções válidas, facilitando a depuração e o desenvolvimento da interface de usuário.

#### 2. Módulo merger.py (Classe Merger)

Este é o coração da aplicação, responsável pela lógica de manipulação dos PDFs.

* Inicialização (__init__): Mantém uma lista de caminhos de arquivo (self.list_of_files), rastreia o estado atual (self.status) e armazena mensagens de erro (self.error_message).
* Gerenciamento de Arquivos: add_file(file_path) adiciona um caminho de arquivo; remove_file(file_path) remove um caminho de arquivo.
* Estrutura de Diretórios (_ensure_directories_exist): Cria as pastas input/ e output/ se elas não existirem.
* Mesclagem Principal (merge_pdfs): Define o status para PROCESSING e utiliza a classe PdfWriter da biblioteca pypdf. Percorre a lista de arquivos, adicionando cada PDF. Salva o arquivo final no output_path. Gerencia o estado, definindo para SUCCESS em caso de êxito ou ERROR se uma exceção ocorrer. Garante que o objeto merger seja fechado no bloco finally.

#### 3. Módulo main.py (Função run_simple_test)

Este módulo é um exemplo de utilização e um mecanismo de teste básico.

* Configuração: Instancia a classe Merger e garante que as pastas de input e output existam.
* Validação de Arquivos: Verifica se os arquivos de teste (requeridos na pasta input/) existem no disco.
* Contagem de Páginas: Calcula o número total de páginas esperado.
* Execução: Chama o método pdf_merger.merge_pdfs().
* Verificação de Resultados: Confirma se o status é SUCCESS, verifica se o arquivo de saída foi criado, e compara o número de páginas obtido com o número de páginas esperado.

---

### Escolha de Arquitetura: Poetry

O projeto é estruturado para ser gerenciado via Poetry.

* Gerenciamento de Dependências: O Poetry isola as dependências (como pypdf) do ambiente global do sistema, garantindo a reprodutibilidade.
* Ambiente Virtual: Gerencia automaticamente um ambiente virtual dedicado.
* Empacotamento Futuro: Simplifica a conversão para um pacote Python distribuível, útil para futuras funcionalidades de CLI e GUI.

---

### Features Futuras Planejadas

As seguintes funcionalidades são prioridades para a próxima fase:

#### 1. Interface de Linha de Comando (CLI) Funcional

* Objetivo: Permitir que o usuário interaja com a ferramenta diretamente pelo terminal.
* Funcionalidades: Comandos para adicionar arquivos por caminho (merger add <file>) e executar a mesclagem (merger run <output_name>). Opções para listar e remover arquivos.

#### 2. Interface Gráfica de Usuário (GUI)

* Objetivo: Oferecer uma maneira mais acessível e visual de usar o programa.
* Tecnologia Sugerida: Uma biblioteca como Tkinter ou Qt (PyQt ou PySide).
* Integração: A GUI utilizará a mesma classe Merger, apenas alterando o módulo main.py.

#### 3. Testes Unitários Abrangentes

* Objetivo: Garantir a estabilidade e a correção do código.
* Foco Principal: Testar a classe Merger, incluindo testes de adição/remoção de arquivos, testes de estado e testes de exceção (simulação de arquivos corrompidos).