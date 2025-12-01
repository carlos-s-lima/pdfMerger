```markdown
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Logo Python" width="50" height="50">

## Projeto de Mesclagem de PDFs em Python

Este documento apresenta a estrutura e as funcionalidades de um projeto em Python voltado para a mesclagem (combinação) de múltiplos arquivos PDF em um único documento. A arquitetura atual é simples e visa a modularidade, facilitando futuras expansões.

---

### Funcionalidades Atuais

O projeto é composto por três módulos principais: status.py, merger.py e main.py.

#### 1. Módulo status.py

* **Definição do Status:** Utiliza a classe Enum do Python para definir um conjunto de estados bem definidos para o processo de mesclagem:
    * WAITING: Estado inicial, aguardando a execução.
    * PROCESSING: A mesclagem está em andamento.
    * SUCCESS: Mesclagem concluída com sucesso.
    * ERROR: Um erro ocorreu durante a mesclagem.
* **Vantagem:** Garante que o estado da operação seja sempre uma das opções válidas, facilitando a depuração e o desenvolvimento da interface de usuário.

#### 2. Módulo merger.py (Classe Merger)

Este é o coração da aplicação, responsável pela lógica de manipulação dos PDFs.

* **Inicialização (\_\_init\_\_)**:
    * Mantém uma lista de caminhos de arquivo (self.list_of_files).
    * Rastreia o estado atual (self.status) inicializado como Status.WAITING.
    * Armazena mensagens de erro (self.error_message).
* **Gerenciamento de Arquivos**:
    * `add_file(file_path)`: Adiciona um caminho de arquivo à lista de mesclagem.
    * `remove_file(file_path)`: Remove um caminho de arquivo da lista, se presente.
* **Estrutura de Diretórios (\_ensure_directories_exist)**:
    * Cria as pastas `input/` e `output/` se elas não existirem, garantindo que o programa tenha locais definidos para entrada e saída.
* **Mesclagem Principal (merge_pdfs)**:
    * Verifica se há arquivos a serem mesclados.
    * Define o status para PROCESSING.
    * Utiliza a classe `PdfWriter` da biblioteca **pypdf** para criar o objeto mesclador.
    * Percorre a lista de arquivos, abrindo cada PDF com `PdfReader` e adicionando-o ao objeto `merger` com `merger.append(reader)`.
    * Salva o arquivo final no `output_path`.
    * Gerencia o estado: Define para SUCCESS em caso de êxito ou ERROR se uma exceção ocorrer, armazenando a mensagem de erro.
    * Garante que o objeto `merger` seja fechado (`merger.close()`) no bloco `finally`, liberando recursos.

#### 3. Módulo main.py (Função run_simple_test)

Este módulo é um exemplo de utilização e um mecanismo de teste básico.

* **Configuração**: Instancia a classe `Merger` e garante que as pastas de `input` e `output` existam.
* **Validação de Arquivos**: Verifica se os arquivos de teste (`teste.pdf` e `lorem-ipsum.pdf` — requeridos na pasta `input/`) existem no disco. Caso contrário, exibe um erro crítico.
* **Contagem de Páginas**: Calcula o número total de páginas esperado (somando as páginas de todos os arquivos de entrada) para fins de verificação pós-mesclagem.
* **Execução**: Chama o método `pdf_merger.merge_pdfs()`.
* **Verificação de Resultados**:
    * Confirma se o status é SUCCESS.
    * Verifica se o arquivo de saída foi criado.
    * Lê o arquivo de saída e compara o número de páginas obtido com o número de páginas esperado.
    * Exibe mensagens detalhadas de sucesso, falha, ou erros de contagem.

---

### Escolha de Arquitetura: Poetry

O projeto é estruturado para ser gerenciado via **Poetry**.

* **Gerenciamento de Dependências:** O Poetry isola as dependências (como `pypdf`) do ambiente global do sistema, garantindo que o projeto seja sempre executado com as versões corretas das bibliotecas. Isso é fundamental para manter a reprodutibilidade.
* **Ambiente Virtual:** Ele gerencia automaticamente um ambiente virtual dedicado, evitando conflitos com outros projetos Python.
* **Empacotamento Futuro:** Embora o projeto seja atualmente um script, o Poetry simplifica a conversão para um pacote Python distribuível, uma etapa útil para as futuras funcionalidades de CLI e GUI.

---

### Features Futuras Planejadas

Em um processo de desenvolvimento iterativo, as seguintes funcionalidades são prioridades para a próxima fase:

#### 1. Interface de Linha de Comando (CLI) Funcional

* **Objetivo:** Permitir que o usuário interaja com a ferramenta diretamente pelo terminal.
* **Funcionalidades:**
    * Comando para adicionar arquivos por caminho (`merger add <file>`).
    * Comando para executar a mesclagem (`merger run <output_name>`).
    * Opções para listar e remover arquivos.

#### 2. Interface Gráfica de Usuário (GUI)

* **Objetivo:** Oferecer uma maneira mais acessível e visual de usar o programa.
* **Tecnologia Sugerida:** Uma biblioteca como **Tkinter** ou **Qt** (via `PyQt` ou `PySide`) para criar uma janela onde o usuário possa arrastar e soltar (drag-and-drop) os arquivos, ordenar a sequência de mesclagem e clicar em um botão para gerar o PDF final.
* **Integração:** A GUI utilizará a mesma classe `Merger` (que é independente de interface), apenas alterando o módulo `main.py` para carregar a interface.

#### 3. Testes Unitários Abrangentes

* **Objetivo:** Garantir a estabilidade e a corretude do código, especialmente antes de adicionar novas funcionalidades.
* **Foco Principal:** Testar a classe `Merger`.
    * **Testes de Adição/Remoção de Arquivos:** Verificar se `add_file` e `remove_file` manipulam a lista corretamente.
    * **Testes de Estado:** Garantir que o `self.status` mude corretamente para WAITING, PROCESSING, SUCCESS e ERROR nos momentos apropriados.
    * **Testes de Mesclagem:** Utilizar arquivos PDF de *mock* (pequenos arquivos criados para teste) para verificar se o número de páginas do arquivo de saída corresponde à soma das páginas dos arquivos de entrada.
    * **Testes de Exceção:** Simular casos de erro (por exemplo, passar um arquivo corrompido ou que não existe) e verificar se o status muda para ERROR e se a mensagem de erro é capturada.
```