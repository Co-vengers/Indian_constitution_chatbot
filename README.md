# Indian Constitution Chatbot

This project is a Flask-based web application that allows users to interact with the text of the Indian Constitution using a conversational chatbot interface powered by Google's Gemini model. The chatbot provides answers to user queries based on the content of the Indian Constitution, which is loaded from a CSV file.

## Features
- **Conversational Chatbot:** Ask questions about the Indian Constitution and receive context-aware answers.
- **Conversation History:** View and manage your previous questions and answers.
- **Delete Conversations:** Remove specific entries from your conversation history.

## Setup Instructions

### Prerequisites
- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- Google Gemini API key (set as `GOOGLE_API_KEY` in your `.env` file)

### Installation
1. **Clone the repository:**
   ```bash
   git clone git@github.com:Co-vengers/Indian_constitution_chatbot.git
   cd Indian_constitution_chatbot
   ```
2. **Install dependencies:**
   ```bash
   pip install flask python-dotenv google-generativeai
   ```
3. **Prepare the environment:**
   - Create a `.env` file in the project root with your Gemini API key:
     ```env
     GOOGLE_API_KEY=your_google_gemini_api_key
     ```
   - Ensure `indian_constitution copy.csv` is present in the project directory.

### Running the App
```bash
python app.py
```
The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## File Structure
- `app.py` — Main Flask application.
- `indian_constitution copy.csv` — CSV file containing the text of the Indian Constitution.
- `conversation_history.json` — Stores conversation history.
- `templates/index.html` — Main HTML template for the web interface.

## Usage
1. Open the app in your browser.
2. Enter your question about the Indian Constitution.
3. View the chatbot's answer and your conversation history.
4. Optionally, delete any conversation entry.

## License
This project is for educational purposes only.
