import os
import google.generativeai as genai
import csv
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for
import json
from functools import lru_cache

# Load environment variables from .env file
load_dotenv()

# Load your API key from the environment variable
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize the Gemini model (outside the request handler for efficiency)
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the path to your permanent CSV file (replace with your actual path)
BOOK_PATH = "/Users/vyomrohila/Documents/coding/Flask/Indian_constitution_chatbot/indian_constitution copy.csv"

app = Flask(__name__)

# Load the book text once at startup
book_text = None

def extract_text_from_csv(csv_path):
    """
    Extracts text from a CSV file.

    Args:
        csv_path: Path to the CSV file.

    Returns:
        The extracted text from the CSV.
    """
    text = ""
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            text += " ".join(row) + "\n"
    return text

# Load the book text once
book_text = extract_text_from_csv(BOOK_PATH)

@lru_cache(maxsize=128)
def get_chatbot_response(user_input):
    """
    Generates a chatbot response based on the user's input and the book's context.

    Args:
        user_input: The user's question or statement.

    Returns:
        The chatbot's response.
    """
    prompt = f"**Context:** {book_text}\n**Question:** {user_input}\n**Answer:**"
    response = model.generate_content(prompt)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def index():
    # Load conversation history from file (if it exists)
    conversation_history = []
    history_file = 'conversation_history.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            conversation_history = json.load(f)

    if request.method == 'POST':
        # Get user query
        user_query = request.form.get('user_query')

        # Get response from the chatbot
        response = get_chatbot_response(user_query)

        # Add current conversation to history
        conversation_history.append({'question': user_query, 'answer': response})

        # Save conversation history to file
        with open(history_file, 'w') as f:
            json.dump(conversation_history, f)

        return render_template('index.html', response=response, conversation_history=conversation_history)

    return render_template('index.html', response=None, conversation_history=conversation_history)

@app.route('/delete_conversation', methods=['POST'])
def delete_conversation():
    try:
        data = request.get_json()
        index_to_delete = data['index']

        with open('conversation_history.json', 'r') as f:
            conversation_history = json.load(f)

        if 0 <= index_to_delete < len(conversation_history):
            del conversation_history[index_to_delete]

            with open('conversation_history.json', 'w') as f:
                json.dump(conversation_history, f)

            return 'Conversation deleted successfully', 200
        else:
            return 'Invalid index', 400 

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return 'Error deleting conversation', 500

if __name__ == '__main__':
    app.run(debug=True)