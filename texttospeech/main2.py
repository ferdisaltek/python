import PyPDF2
from gtts import gTTS

from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_reader = PdfReader(pdf_path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text






def text_to_audiobook(text, output_file, language='en', speed=1):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)


pdf_path = '/Users/ferdisaltek/Downloads/stories.pdf'
audiobook_output = '/Users/ferdisaltek/Downloads/output_audiobook.mp3'  # You can change the output format if needed (e.g., .m4a)

text = extract_text_from_pdf(pdf_path)
text_to_audiobook(text, audiobook_output)
