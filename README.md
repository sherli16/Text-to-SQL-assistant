# Text-to-SQL Assistant

Type in English -> Get Answer from Database

Ask questions in plain English, this app converts it to SQL using Gemini AI and fetches answers from SQLite Database.

## Features

- Ask questions in English
- Auto generates SQL using Gemini AI
- Shows Generated SQL + Answer Table
- Built with Streamlit

## Tech Stack

- Python
- Streamlit
- SQLite
- LangChain
- Google Gemini

## Setup
### 1. Install Dependencies
pip install streamlit python-dotenv langchain-google-genai

### 2. Create .env File
GOOGLE_API_KEY=your_api_key_here

### 3.Create Database
Db.py

### 4.Run APP
streamlit run text_SQL.py

### Eg Questions:
How many employees in Chennai?
Show all IT employees in Coimbatore
Who has highest salary?
