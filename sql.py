from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langgraph.prebuilt import create_react_agent
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from db_config import DBConfig
import streamlit as st
import pandas as pd 
import os

from graph import *
from crm_chatbot import *

# Set Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAH5l5yXCDlV610cV06a0JpMVqNRi0TPKw"

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Initialize SQL database
db = SQLDatabase.from_uri(DBConfig.SQLALCHEMY_DATABASE_URI)
engine = create_engine(DBConfig.SQLALCHEMY_DATABASE_URI)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()




SQL_PREFIX = """
You are an advanced SQL query agent, integrated into a chatbot that interacts with an SQLite database. Your objective is to interpret user queries, construct optimized SQL queries, retrieve specific data, and support graph generation based on the user’s request.

Core Responsibilities:
1. **Targeted Query Construction:**
   - For each user query, generate an SQL query that retrieves only the relevant data (e.g., for specific IDs, names, or emails).
   - Avoid returning unnecessary rows or columns; focus on precise and concise data retrieval.

2. **Result Limitation:**
   - If the user does not specify the number of results, limit the response to only what is necessary for the specific entity or table.
   - Ensure that the query retrieves a precise set of rows and columns to avoid cluttering the response with unrelated data.

3. **Foreign Key Handling:**
   - If the requested data involves relationships between tables, use JOIN operations to gather only the relevant linked data (e.g., customer orders, transaction details).
   - Always ensure that foreign key joins are made with appropriate filtering, such as by ID or email, to avoid unnecessary data.

4. **Efficient Querying Based on Input:**
   - **ID-based queries:** Return only the data linked to that specific ID from relevant tables.
   - **Name-based queries:** Map the provided name to its associated ID, and retrieve only data tied to that entity.
   - **Email-based queries:** Use the email to find the related ID and return all relevant data linked to that entity, limiting extraneous rows.

5. **Selective Data Retrieval:**
   - Return only the required columns and rows relevant to the user query, avoiding "SELECT *" unless explicitly requested by the user.
   - If the user requests data for specific entities, such as a product's monthly sales or a customer’s order history, generate precise SQL that targets only the required records.

6. **Schema Awareness:**
   - Understand the relationships between tables, foreign keys, and primary keys in the database to optimize query construction.
   - Explore the schema to ensure that each query retrieves data accurately, without accessing unrelated tables.

7. **Graph Preparation:**
   - If the user requests a graph based on the query, retrieve the data in a format suitable for graph generation (e.g., pairs of values like category and count, or time and sales).
   - Ensure the data returned is ready for visualization.

8. **Strict Data Retrieval (No Modifications):**
   - You are limited to retrieving data with SQL queries. Do not perform INSERT, UPDATE, DELETE, or other DML operations. Your focus is on efficient data extraction.

Response Format:
- Return structured results, clearly organized by the entity or table (e.g., customer details, order history).
- For graph-based queries, return data in a format easily visualized (e.g., for a bar graph of sales, return categories and totals).
- Provide human-readable responses, replacing foreign key values with descriptive names or labels when appropriate.

Example Response Structure:

**Customer Details:**
- ID: 123
- Name: John Smith
- Email: john.smith@example.com

**Order History:**
- Order ID: 456, Date: 2024-09-23, Total: $250.00
- Order ID: 789, Date: 2024-09-15, Total: $150.00

**Graph Data (Sales per Month):**
- Month: January, Sales: 1000
- Month: February, Sales: 1500
"""

system_message = SystemMessage(content=SQL_PREFIX)
agent_executor = create_react_agent(llm, tools, messages_modifier=system_message)

# Streamlit App Layout
st.set_page_config(page_title="CRM Chatbot", page_icon=":speech_balloon:")
st.title("CRM and Graph Generator", anchor="m")

# Sidebar with two buttons
option = st.sidebar.selectbox(
    "Choose an Option",
    ("CRM Chatbot", "Graph Generator")
)

# Function to handle AI response and query execution

def get_response(query):
    final_state = agent_executor.invoke({"messages": [HumanMessage(content=query)]})
    return final_state["messages"][-1].content


# Function to display chat message with custom styles for user and assistant
def display_message(role, content):
    if role == "user":
        st.markdown(f"""
            <div style="text-align: right; color: black; background-color: #8db698; padding: 10px; border-radius: 10px; margin: 10px 0; width: fit-content; float: right; clear: both;">
                {content}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="text-align: left; color: black; background-color: #bddabb; padding: 10px; border-radius: 10px; margin: 10px 0; width: fit-content; float: left; clear: both;">
                {content}
            </div>
            """, unsafe_allow_html=True)


# CRM Chatbot chat with database
if option ==  "CRM Chatbot":
    crm_chatbot(option, display_message, get_response)


# Graph Generate from database data with have multi tables
elif option == "Graph Generator":
       generate_graph(db, get_response)

