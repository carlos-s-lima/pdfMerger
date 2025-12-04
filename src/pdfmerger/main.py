import sys
from merger import Merger     
from status import Status     
from files import PdfFile
from cli_utils import setup_argparse, get_unique_output_path

def main():
    args = setup_argparse()
    final_output_path = get_unique_output_path(args.output)
    
    pdf_merger = Merger()

    print("--- INICIANDO PROCESSO DE MESCLAGEM ---\n")

    total_paginas_previstas = 0
    arquivos_validos = True
    
    for file_path in args.files:
        try:
            pdf_file = PdfFile(file_path)
            pdf_merger.add_file(pdf_file)
            print(f"[OK] Adicionado: {pdf_file.path.name} ({pdf_file.page_count} páginas)")
            total_paginas_previstas += pdf_file.page_count
        except FileNotFoundError:
            print(f"[ERRO] Arquivo não encontrado: {file_path}")
            arquivos_validos = False
            break
        except Exception as e:
            print(f"[ERRO] Falha ao processar {file_path}: {e}")
            arquivos_validos = False
            break

    if not arquivos_validos:
        sys.exit(1)

    print(f"\nTotal de arquivos: {len(pdf_merger.list_of_files)}")
    print(f"Total de páginas esperadas: {total_paginas_previstas}")
    print(f"\nMesclando para: {final_output_path} ...")
    pdf_merger.merge_pdfs(final_output_path) 
    
    if pdf_merger.status == Status.SUCCESS.value:
        print(f"\n>>> SUCESSO! Mesclagem concluída. Arquivo gerado em: {final_output_path}")
    else:
        print(f"\n>>> FALHA. Motivo: {pdf_merger.error_message}")
        sys.exit(1)

if __name__ == "__main__":
    main()