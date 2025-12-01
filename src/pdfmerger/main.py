import os
import sys
from pathlib import Path
from pypdf import PdfWriter, PdfReader
from merger import Merger     
from status import Status     

def run_simple_test():
    
    pdf_merger = Merger()
    
    pdf_merger._ensure_directories_exist() 
    
    REAL_PDF_1 = "input/teste.pdf" 
    REAL_PDF_2 = "input/lorem-ipsum.pdf"
    
    OUTPUT_FILE = "merged-pdf.pdf"
    
    output_path_full = Path("output") / OUTPUT_FILE
    if output_path_full.exists():
        os.remove(output_path_full)
    
    print("\n--- INICIANDO TESTE DE MESCLAGEM (Arquivos Reais) ---")

    test_files = [
        REAL_PDF_1,
        REAL_PDF_2
    ]
    
    num_paginas_esperado = 0
    arquivos_validos = True
    
    for f_path in test_files:
        if not Path(f_path).exists():
            print(f"ERRO CRÍTICO: Arquivo não encontrado no caminho: {f_path}")
            print("Por favor, coloque este PDF dentro da pasta 'input'.")
            arquivos_validos = False
            break
        
        pdf_merger.add_file(f_path)
        
        try:
            num_paginas_esperado += len(PdfReader(f_path).pages)
        except Exception:
            print(f"AVISO: Não foi possível ler as páginas de {f_path}. Pode estar corrompido.")
            
    if not arquivos_validos:
        sys.exit(1)

    print(f"\nArquivos na lista da classe: {len(pdf_merger.list_of_files)}")
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