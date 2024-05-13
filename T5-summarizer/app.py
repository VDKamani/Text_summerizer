from flask import Flask, render_template, request
from email_summarizer.email_summarizer import summarize_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        if 'email_text' in request.form:
            text = request.form['email_text']
            summary = summarize_email(text)
            return summary  # This line returns only the summary text, not the full HTML page
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)