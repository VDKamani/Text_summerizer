# Text-Summarizer
Text Summarization using T5 Algorithm 

# Text Summarizer Web Page

A user-friendly web page that summarizes text either entered directly into a text box or uploaded as a file. Utilizing the powerful T5 summarizer model at its core, this tool provides you with a precise and concise summary of the provided text. Experience the efficiency of automated summarization and enhance your productivity.

## Features

- Summarize text entered directly into a text box.
- Summarize text from uploaded files.
- Utilizes T5 summarizer model for precise summaries.
- Easy-to-use interface with HTML, CSS, and JavaScript.
- Backend powered by Python.

## Technology Used

- HTML
- CSS
- JavaScript
- Python

## What is T5 Algorithm?

The T5 (Text-To-Text Transfer Transformer) algorithm is a powerful language model developed by Google Research. It is designed to convert various natural language processing (NLP) tasks into a unified text-to-text format, allowing it to handle a wide range of tasks with a single model. This model excels in extractive summarization, meaning it generates summaries by identifying and extracting key information from the source text.

## Installation

To run this project locally, follow these steps:

### Prerequisites

Ensure you have the following installed:

- Python 3.6 or higher
- Pip (Python package installer)

### Clone the Repository

Install Required Libraries
- pip install transformers
- pip install PyPDF2
- pip install sentencepiece
- pip install flask

### Usage
Run the Flask Server

- In the project directory, run:
- python app.py
- This will start the Flask server on http://127.0.0.1:5000/.
- Open the Web Page- Open your web browser and navigate to http://127.0.0.1:5000/. You will see the text summarizer web page.
- Summarize Text
- Direct Text Input: Enter text directly into the text box and click the "Summarize" button to get the summary.
- File Upload: Upload a text file (e.g., .pdf) and click the "Summarize" button to get the summary.

### Project Structure

- text-summarizer-webpage/
- │
- ├── app.py                  # Flask application
- ├── templates/
- │   └── index.html          # HTML file for the web page
- ├── static/
- │   ├── css/
- │        └── styles.css      # CSS file for styling
- └── README.md               # This README file


### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bugs, improvements, or features.

### Viral D. Kamani 
### Happy Learning!!!