import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can access the API key
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("There is a person who is going to tell you how they feel. I want you to display a corresponding bible verse that relates"
    " to what there feeling and helps them out. Please reference it. The other person response: Im feeling very stressed because of my exams")
print(response.text)