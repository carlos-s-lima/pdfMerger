from typing import List
from status import Status
from pypdf import PdfReader, PdfWriter
import os
from pathlib import Path

class Merger:
    
    def __init__(self):
        
        self.list_of_files: List[str] = []
        self.status: str = Status.WAITING.value
        self.error_message:str = ""

    def _ensure_directories_exist(self):
        
        input_dir = "input"
        output_dir = "output"
        Path(input_dir).mkdir(exist_ok=True)
        Path(output_dir).mkdir(exist_ok=True)

    def add_file(self, file_path: str) -> None:
        
        self.list_of_files.append(file_path)

    def remove_file(self, file_path: str) -> None:
        
        if file_path in self.list_of_files:
            self.list_of_files.remove(file_path)

    def merge_pdfs(self, output_path: str) -> None:
        
        self._ensure_directories_exist()
       
        if not self.list_of_files:
            self.status = Status.ERROR.value
            self.error_message = "No files to merge."
            return
        
        merger = PdfWriter()
        
        try:
            self.status = Status.PROCESSING.value
            
            for file_path in self.list_of_files:
                reader = PdfReader(file_path)
                merger.append(reader)
            merger.write(output_path)
            self.status = Status.SUCCESS.value
            self.error_message = ""
        
        except Exception as e:
            self.status = Status.ERROR.value
            self.error_message = f"Error merging files: {str(e)}"

        finally:
            merger.close()