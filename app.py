import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    load_dotenv()  # Load environment variables
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)
    # Retrieve the response from query parameters
    response = request.args.get('response')
    return render_template('index.html', response=response)

@app.route('/submit', methods=['POST'])
def submit():
    textarea_content = request.form.get('textarea')  # Get the content of the textarea
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        ("A person is about to share their feelings. Please provide a relevant Bible verse that addresses their emotions and offers support. "
        "Make sure to reference the verse. "
        "After this please provide a explanation for the verse. "
        "After this please provide ways to practice this verse. "
        "If the response below has nothing to do with emotions, religion, how they are feeling, or a verse they dont want you to use please respond with 'Not Applicable'. "
        + textarea_content)
    )
    response_text = response.text if hasattr(response, 'text') else str(response)
    response_split = response_text.splitlines()
    
    # Convert the list to a single string with a delimiter
    response_html = "<br>".join(response_split)  # Use <br> for line breaks in HTML

    return redirect(url_for('home', response=response_html))

if __name__ == "__main__":
    app.run(debug=True)
