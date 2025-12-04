import os
import sys
from pathlib import Path
from pypdf import PdfWriter, PdfReader
from merger import Merger     
from status import Status     
from files import PdfFile

def run_simple_test():
    
    pdf_merger = Merger()
    pdf_merger._ensure_directories_exist() 
    
    REAL_PDF_1_PATH = "input/teste.pdf" 
    REAL_PDF_2_PATH = "input/lorem-ipsum.pdf"
    
    OUTPUT_FILE = "merged-pdf-test2.pdf"
    
    output_path_full = Path("output") / OUTPUT_FILE
    
    if output_path_full.exists():
        os.remove(output_path_full)
    
    print("\n--- INICIANDO TESTE DE MESCLAGEM (Arquivos Reais com POO) ---")

    test_file_paths = [
        REAL_PDF_1_PATH,
        REAL_PDF_2_PATH
    ]
    
    num_paginas_esperado = 0
    arquivos_validos = True
    
    for f_path in test_file_paths:
        
        try:
            pdf_file_obj = PdfFile(f_path) 
            pdf_merger.add_file(pdf_file_obj)
            num_paginas_esperado += pdf_file_obj.page_count
            
        except FileNotFoundError as e:
            print(f"ERRO CRÍTICO: {e}")
            print("Por favor, coloque este PDF dentro da pasta 'input'.")
            arquivos_validos = False
            break
        except Exception as e:
            print(f"AVISO: Erro ao processar o arquivo {f_path}. {e}")
            
    if not arquivos_validos:
        sys.exit(1)

    print(f"\nArquivos (objetos) na lista da classe: {len(pdf_merger.list_of_files)}")
    print(f"Status inicial: {pdf_merger.status}")
    
    pdf_merger.merge_pdfs(str(output_path_full)) 

    print("\n--- RESULTADOS ---")
    
    if pdf_merger.status == Status.SUCCESS.value:
        print("Status: SUCESSO. Mesclagem concluída!")
        
        if output_path_full.exists():
            print(f"Arquivo final encontrado em: {output_path_full}")
            try:
                final_reader = PdfReader(output_path_full)
                paginas_obtidas = len(final_reader.pages)
                
                print(f"Páginas mescladas: {paginas_obtidas}")
                print(f"(Total esperado: {num_paginas_esperado})")
                
                if paginas_obtidas != num_paginas_esperado:
                    print(f"ERRO DE CONTAGEM: O número de páginas obtido ({paginas_obtidas}) não corresponde ao esperado ({num_paginas_esperado}).")

            except Exception as e:
                print(f"Erro ao ler o arquivo final: {e}")
        else:
            print("ERRO: O arquivo final não foi criado no disco.")
                
    else:
        print(f"Status: FALHA. (Esperado: {Status.SUCCESS.value})")
        print(f"Erro da aplicação: {pdf_merger.error_message}")

if __name__ == "__main__":
    run_simple_test()