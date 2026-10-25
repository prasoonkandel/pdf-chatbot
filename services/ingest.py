import pdfplumber

from services.chunk import chunk

file = "test_data/clean_text.pdf"


with pdfplumber.open(file) as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"====== Page {i + 1} ======")
        text = page.extract_text()
        print(text)
        print("------ Chunks ------")
        for i, item in enumerate(chunk(text)):
            print(f"{i + 1}. {item}")
        print("\n\n")
        print("============")
