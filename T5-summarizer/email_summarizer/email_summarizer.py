from transformers import T5Tokenizer, T5ForConditionalGeneration
from PyPDF2 import PdfFileReader

class EmailSummarizer:
    def __init__(self, text, num_sentences=3):
        self.text = text
        self.num_sentences = num_sentences

    def summarize(self):
        return self._summarize_with_t5(self.text)

    def _summarize_with_t5(self, text):
        tokenizer = T5Tokenizer.from_pretrained("t5-base")
        model = T5ForConditionalGeneration.from_pretrained("t5-base")
        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    
    @staticmethod
    def extract_text_from_pdf(pdf_file):
        try:
            pdf_text = ""
            with pdf_file as f:
                pdf_reader = PdfFileReader(f)
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    page_text = page.extractText()
                    pdf_text += page_text + "\n"
            return pdf_text.strip()
        except Exception as e:
            print("Error extracting text from PDF:", e)
            return ""

def summarize_email(text, num_sentences=3):
    summarizer = EmailSummarizer(text, num_sentences)
    return summarizer.summarize()
