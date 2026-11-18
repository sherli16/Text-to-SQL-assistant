import streamlit as st
import sqlite3
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.title("Text-to-SQL Assistant")
st.write("Type in English -> Get Answer from Database")
# Database Schema
SCHEMA = """
Table: employees
Columns:
- id (INTEGER)
- name (TEXT)
- department (TEXT)
- salary (INTEGER)
- city (TEXT)
"""

question = st.text_input("Enter your question:", placeholder="Ex: Show all IT employees in Coimbatore")

if question:
    with st.spinner("Create SQL"):
        llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0)

        prompt = f"""
        You are a SQL expert. Convert the question to SQLite SQL query.
        Use ONLY this schema:
        {SCHEMA}

        Rules:
        - Return ONLY SQL query, no explanation, no markdown
        - Use SELECT only

        Question: {question}
        SQL:
        """
        result = llm.invoke(prompt)
        raw = result.content
        if isinstance(raw, list):
            first = raw[0]
            if isinstance(first, dict):
                raw = first.get("text", "")
            elif hasattr(first, "text"):
                raw = first.text
            else:
                raw = str(first)

        sql_query = raw.strip().replace("```sql", "").replace("```", "").strip()

        st.subheader("Generated SQL:")
        st.code(sql_query, language="sql")

        # 2. SQL ah Run pannu ma
        try:
            conn = sqlite3.connect("company.db")
            cur = conn.cursor()
            cur.execute(sql_query)
            rows = cur.fetchall()
            columns = [d[0] for d in cur.description]
            conn.close()

            st.subheader("Answer:")
            if rows:
                st.table([dict(zip(columns, r)) for r in rows])
            else:
                st.write("No data found!")
        except Exception as e:
            st.error(f"SQL Error: {e}")