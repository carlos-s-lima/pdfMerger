import argparse
from pathlib import Path

def setup_argparse():
    parser = argparse.ArgumentParser(
        description="Ferramenta CLI para mesclagem de PDFs."
    )
    
    parser.add_argument(
        'files', 
        nargs='+', 
        help='Caminhos dos arquivos PDF a serem mesclados (em ordem).'
    )
    
    parser.add_argument(
        '-o', '--output', 
        default='output/merged_cli.pdf',
        help='Caminho/Nome do arquivo de saída (Padrão: output/merged_cli.pdf)'
    )
    
    return parser.parse_args()

def get_unique_output_path(base_path_str: str) -> str:
    """
    Garante que o diretório de saída exista e retorna um caminho indexado 
    (ex: merged_cli_1.pdf) se o arquivo já existir.
    """
    base_path = Path(base_path_str)
    base_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not base_path.exists():
        return base_path_str

    suffix = base_path.suffix
    stem = base_path.stem
    
    counter = 1
    new_path = base_path
    
    while new_path.exists():
        new_filename = f"{stem}_{counter}{suffix}"
        new_path = base_path.with_name(new_filename)
        counter += 1
        
    return str(new_path)