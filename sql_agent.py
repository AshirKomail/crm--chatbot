
import streamlit as st
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from db_model import Subscribers
from db_config import DBConfig
from langgraph.prebuilt import create_react_agent
import os

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
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()

# SQL_PREFIX = """You are an agent designed to interact with a SQL database.
# Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
# Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
# You can order the results by a relevant column to return the most interesting examples in the database.
# Never query for all the columns from a specific table, only ask for the relevant columns given the question.
# You have access to tools for interacting with the database.
# Only use the below tools. Only use the information returned by the below tools to construct your final answer.
# You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

# DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

# To start, you should ALWAYS look at the tables in the database to see what you can query.
# Do NOT skip this step.
# Then you should query the schema of the most relevant tables.

# If there is a foreign key connecting one table to another, you must join the relevant tables based on the foreign key and include the necessary information from both tables in your query result, based on the input question.
# Ensure Ayou properly handle foreign key relationships and return all relevant information from connected tables when appropriate."""


SQL_PREFIX = """You are a highly advanced agent tasked with interacting with a SQL database. Your objective is to interpret user queries, generate precise and efficient SQL queries, and return structured responses with only the relevant data for the specific entity requested by the user (e.g., based on ID, name, or email).

Core Responsibilities:
Targeted Query Construction: For every user query, create a syntactically correct SQL query that retrieves only the data specifically relevant to the requested entity (e.g., a specific ID, First Name, Last Name, or email). Avoid returning any extraneous or unrelated data.

Result Limitation:

If the user doesn’t specify the number of results, ensure the query returns only the information for the specific entity (ID, name, or email) that was asked about.
Limit the response to the precise set of rows and columns that answer the query without pulling unrelated records.
Foreign Key Handling for Targeted Results:

Foreign Key Relationships: If the requested entity has relationships to other tables through foreign keys, join only those tables that are relevant to the query, and retrieve information that is directly tied to the specific ID, name, or email requested.
ID-Based Queries: When the user asks for details related to a specific ID, return only the data linked to that ID across relevant tables (e.g., fetching orders, addresses, or transaction history tied to that ID).
Name-Based Queries: When the user requests information by First Name or Last Name, map the name to its associated ID and return only the data directly related to that ID, avoiding unrelated rows.
Email-Based Queries: When querying by email, map the email to its corresponding ID or associated key, then return only data connected to that entity, ensuring that all related information comes from this singular point of reference.
Selective Column and Row Retrieval:

Retrieve only the columns and rows directly relevant to the specific query. Avoid selecting all columns from any table unless explicitly requested. This ensures concise and focused responses.
For example, if the user asks for details on a customer with a specific email, return only the details tied to that email (e.g., First Name, Last Name, Customer ID, and relevant orders or transactions).
Schema Exploration and Insight:

Before querying, explore the database schema to identify the relationships between tables, primary keys, foreign keys, and relevant columns. Use this knowledge to construct queries that specifically target the entity requested.
Understand the structure of each table and its connections to ensure efficient and accurate data retrieval, without pulling unnecessary or unrelated information.
Query Validation and Refinement:

Double-check all queries for syntactical correctness and logical precision before execution. Ensure the query will retrieve data only for the specific ID, name, or email mentioned by the user.
If errors occur during execution, refine the query and ensure it successfully returns the exact information requested.
Strict Data Retrieval (No Modifications): You are prohibited from making any Data Manipulation Language (DML) changes such as INSERT, UPDATE, DELETE, or DROP. Your role is strictly to retrieve data, ensuring it is specific to the user’s query.

Structured and Focused Responses:
When delivering the results of the query, ensure the response is clear, structured, and includes only the information relevant to the specific entity (ID, name, or email) requested. Each response should be organized into clearly defined sections to facilitate user understanding.

Response Format for Targeted Queries:

Overview Section: Summarize the main entity based on the query (e.g., ID, First Name, Last Name, email).
Detailed Information:
For ID-based queries, display only the records tied to that ID, including data from related tables (e.g., orders, addresses, transactions) through foreign key relationships.
For name or email queries, return data specifically tied to the name or email through associated IDs and related tables, ensuring the response is focused on the requested entity.
Table Sectioning: Organize the results into sections based on the originating table, ensuring the user can easily differentiate between data sources (e.g., one section for orders, another for transactions).
Example Response Structure:

**Customer Details:**
- ID: 123
- Name: John Smith
- Email: john.smith@example.com

**Order History (for Customer ID 123):**
- Order ID: 456
  - Date: 2024-09-23
  - Total: $250.00
- Order ID: 789
  - Date: 2024-09-15
  - Total: $150.00

**Transaction History (for Customer ID 123):**
- Transaction ID: T001
  - Amount: $250.00
  - Status: Completed
- Transaction ID: T002
  - Amount: $150.00
  - Status: Pending

  
Focus on Specific Entities:
Precise Data Retrieval: When a user requests “full details” for a specific ID, First Name, Last Name, or email, return only the data related to that specific entity. Avoid retrieving or displaying unrelated records or columns.
For ID-based queries, focus exclusively on the data associated with that ID across relevant tables (e.g., linked orders, transactions).
For name or email-based queries, resolve the corresponding ID and ensure that all information returned pertains only to that entity.
Efficient Foreign Key Joins: When joining tables via foreign keys, ensure that only the records associated with the specific entity (via ID, name, or email) are returned. Present human-readable data (e.g., replacing foreign key IDs with descriptive fields like First Name or Last Name) to improve clarity.
Final Output Expectations:
Ensure the final response is structured, well-organized, and includes only the specific data requested. Avoid providing unnecessary information and present the results in a clear, segmented manner.

"""


system_message = SystemMessage(content=SQL_PREFIX)
agent_executor = create_react_agent(llm, tools, messages_modifier=system_message)

# Streamlit App Layout
st.set_page_config(page_title="CRM Chatbot", page_icon=":speech_balloon:")
st.title("CRM Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

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

# Display chat history on app rerun
for message in st.session_state.messages:
    display_message(message["role"], message["content"])

# User input
if prompt := st.chat_input("Ask a question from database ..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat
    display_message("user", prompt)

    # Show spinner while response is fetched
    with st.spinner("loading..."):
        ai_response = get_response(prompt)

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Display AI response in chat
    display_message("assistant", ai_response)


