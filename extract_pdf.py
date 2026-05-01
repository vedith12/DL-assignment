import sys
import subprocess
try:
    from pypdf import PdfReader
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    from pypdf import PdfReader

def extract(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n---PAGE BREAK---\n"
    with open("pdf_format.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    extract("Dog-Breed-Classification-Using-Deep-Learning.pdf")
