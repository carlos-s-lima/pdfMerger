from pathlib import Path
from pypdf import PdfReader

class PdfFile:

    def __init__ (self, path: str):
        self.path = Path(path)
        self.reader = None
        self._page_count = 0

        if not self.path.exists() or not self.path.is_file():
            raise FileNotFoundError(f"File not found: {self.path}")
        
        try:
            reader = PdfReader(self.path)
            self._page_count = len(reader.pages)
        except Exception as e:
            print(f"WARNING: Could not read the PDF file {self.path.name}. {e}")

    @property
    def page_count(self) -> int:
        return self._page_count
    
    def get_reader(self) -> PdfReader:
        if self.reader is None:
            try:
                self.reader = PdfReader(self.path)
            except Exception as e:
                print(f"ERROR: Unable to create PdfReader for {self.path.name}. {e}")
        return self.reader
    
    def __str__(self):
        return f"PDF File: {self.path.name}, Pages: {self.page_count}"