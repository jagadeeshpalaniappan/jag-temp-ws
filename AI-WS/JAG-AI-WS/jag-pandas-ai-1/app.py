import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
from langchain_community.llms import Ollama 
import sqlite3
import os

llm = Ollama(model="llama3")

# Excel
# df = pd.read_excel('data.xlsx')

# CSV:
# df = pd.read_csv('data.csv')

# DB:
conn = sqlite3.connect('data.db')
df = pd.read_sql('SELECT * FROM countries', conn)
conn.close()


df = SmartDataframe(df, config={"llm": llm})

print( df.chat('Which are the 5 happiest countries?'))

print('-------------------')

print( df.chat('What is the sum of the GDPs of the 2 happiest countries?'))