import PyPDF2
import pyttsx3

from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_reader = PdfReader(pdf_path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text



def text_to_speech(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    
if __name__ == "__main__":
    pdf_path = "/Users/ferdisaltek/Downloads/stories.pdf"
    output_path = "/Users/ferdisaltek/Downloads/output_audiobook.mp3"

    extracted_text = extract_text_from_pdf(pdf_path)
    text_to_speech(extracted_text, output_path)

    print(f"Audiobook saved to {output_path}")
