import sys
import PyPDF2

def extract_text(pdf_path, txt_path):
    try:
        reader = PyPDF2.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            extr = page.extract_text()
            if extr: text += extr + "\n"
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Successfully extracted {len(reader.pages)} pages to {txt_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_text(sys.argv[1], sys.argv[2])
