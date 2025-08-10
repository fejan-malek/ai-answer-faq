# AI Answer FAQ – Titanic SQL Chatbot

This project demonstrates how to use **LangChain** with **Google Generative AI** to query a Titanic dataset stored in a SQLite database using natural language.

## Tech Stack
- **Python** (pandas, sqlite3, dotenv)
- **LangChain** (SQL Agent Toolkit, SQLDatabase)
- **Google Generative AI API**
- **SQLite**
- **Pandas**

## Model Used
- **gemini-2.0-flash** (via `ChatGoogleGenerativeAI`)

## How It Works
1. Load Titanic dataset (`titanic.csv`) into a pandas DataFrame.
2. Store the dataset into a local SQLite database (`titanic.db`).
3. Use LangChain’s SQL Agent to connect an LLM to the database.
4. Query the database in plain English (e.g., "What's the total of survivors with male and female?").


## Run

```bash
python titanic.py
```

## Top 5 Questions

1. What's the **average age** of survivors?  
2. What's the **total number of survivors grouped by gender** (male and female)?  
3. What's the **survival rate** for each passenger class (1st, 2nd, 3rd)?  
4. How many **children (age < 18)** survived, grouped by gender?  