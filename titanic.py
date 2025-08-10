import os
import pandas as pd
import sqlite3
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase

# Load CSV into pandas DataFrame
df = pd.read_csv("titanic.csv")

# Create SQLite database and load DataFrame into it
conn = sqlite3.connect("titanic.db")
df.to_sql("titanic", conn, if_exists="replace", index=False)
conn.close()

# Set your Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBaqV9D9meX_2BFHB9Zx6l5Sh7IlD-nfM8"

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

# Wrap SQLite DB for LangChain
db = SQLDatabase.from_uri("sqlite:///titanic.db")

# Create SQL agent
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

# Run query
# agent_executor.invoke({"input": "what's the average age of survivors"})
agent_executor.invoke({"input": "what's the total of surviour with male and female?"})
