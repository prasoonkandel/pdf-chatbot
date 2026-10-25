from enum import EnumMeta

import pdfplumber

file = "test_data/table_data.pdf"


with pdfplumber.open(file) as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"--- Page {i + 1} ---")
        print(page.extract_text())
        print("------")
