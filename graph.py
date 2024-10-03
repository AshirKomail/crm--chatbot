# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# from sqlalchemy import text
# import re

# def generate_graph(db, get_response):
#     st.subheader("Graph Generator")

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:
#         display_message(message["role"], message["content"])

#     if prompt := st.chat_input("Ask for a graph from the database..."):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         display_message("user", prompt)

#         if "graph" in prompt.lower():
#             with st.spinner("Loading..."):
#                 data = fetch_data_for_graph(prompt, db)

#             if data is not None:
#                 graph_types = process_prompt_for_graph(prompt)
#                 for graph_type in graph_types:
#                     x_col, y_col = determine_columns(graph_type, data.columns)
#                     if x_col and y_col:
#                         display_graph(data, x_col, y_col, graph_type)
#                     else:
#                         st.write(f"Could not determine the columns for {graph_type}.")
#             else:
#                 st.write("No data available for the graph.")
#         else:
#             with st.spinner("Fetching response..."):
#                 ai_response = get_response(prompt)
#             st.session_state.messages.append({"role": "assistant", "content": ai_response})
#             display_message("assistant", ai_response)

# def fetch_data_for_graph(prompt, db):
#     table_names = db.get_table_names()
#     selected_table = next((table for table in table_names if table in prompt), None)

#     if selected_table is None:
#         st.error("No valid table name found in the prompt.")
#         return None

#     row_limit = None
#     if "first" in prompt.lower():
#         match = re.search(r"first (\d+)", prompt.lower())
#         if match:
#             row_limit = int(match.group(1))

#     query = f"SELECT * FROM {selected_table}"
#     if row_limit:
#         query += f" LIMIT {row_limit}"

#     try:
#         with db._engine.connect() as conn:
#             result = conn.execute(text(query))
#             data = result.fetchall()
#         df = pd.DataFrame(data, columns=result.keys())
#         return df
#     except Exception as e:
#         st.error(f"An error occurred while fetching data: {e}")
#         return None

# def process_prompt_for_graph(prompt):
#     graph_types = []
#     if "bar" in prompt.lower():
#         graph_types.append("Bar Graph")
#     if "line" in prompt.lower():
#         graph_types.append("Line Graph")
#     if "pie" in prompt.lower():
#         graph_types.append("Pie Chart")
#     if "scatter" in prompt.lower():
#         graph_types.append("Scatter Plot")
#     if "histogram" in prompt.lower():
#         graph_types.append("Histogram")
    
#     # If no specific graph type is found, default to bar graph
#     if not graph_types:
#         graph_types.append("Bar Graph")
        
#     return graph_types

# def determine_columns(graph_type, columns):
#     x_col = None
#     y_col = None

#     if "id" in columns:
#         x_col = 'id'
#     if "campaign_id" in columns:
#         y_col = 'campaign_id'

#     return x_col, y_col

# def display_graph(data, x_col, y_col, graph_type):
#     st.subheader(f"Generated {graph_type}")

#     if not data.empty:
#         fig, ax = plt.subplots(figsize=(10, 6))

#         if graph_type == "Bar Graph":
#             bars = ax.bar(data[x_col], data[y_col], color='skyblue')
#             for bar in bars:
#                 yval = bar.get_height()
#                 ax.text(bar.get_x() + bar.get_width() / 2, yval, 
#                         f'{yval}', ha='center', va='bottom', color='black')

#         elif graph_type == "Line Graph":
#             ax.plot(data[x_col], data[y_col], marker='o', color='skyblue')

#         elif graph_type == "Pie Chart":
#             ax.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%', colors=plt.cm.Paired.colors)

#         elif graph_type == "Scatter Plot":
#             ax.scatter(data[x_col], data[y_col], color='skyblue')

#         elif graph_type == "Histogram":
#             ax.hist(data[y_col], bins=10, color='skyblue', edgecolor='black')

#         if graph_type != "Pie Chart":
#             ax.set_xlabel(x_col, color='white')
#             ax.set_ylabel(y_col, color='white')
#             ax.set_title(f"{graph_type} of {y_col} vs {x_col}", color='white')

#         plt.gcf().set_facecolor(color="blacK")
#         st.pyplot(fig)
#     else:
#         st.write("No data available for graph generation.")

# def display_message(role, content):
#     if role == "user":
#         st.markdown(f"""
#             <div style="text-align: right; color: black; background-color: #8db698; padding: 10px; border-radius: 10px; margin: 10px 0; width: fit-content; float: right; clear: both;">
#                 {content}
#             </div>
#             """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#             <div style="text-align: left; color: black; background-color: #bddabb; padding: 10px; border-radius: 10px; margin: 10px 0; width: fit-content; float: left; clear: both;">
#                 {content}
#             </div>
#             """, unsafe_allow_html=True)



import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import text
import re

def generate_graph(db, get_response):
    st.subheader("Graph Generator")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        display_message(message["role"], message["content"])

    if prompt := st.chat_input("Ask for a graph from the database..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        display_message("user", prompt)

        if "graph" in prompt.lower():
            with st.spinner("Loading..."):
                data = fetch_data_for_graph(prompt, db)

            if data is not None:
                graph_types = process_prompt_for_graph(prompt)
                # Identify x and y columns for all graph types
                for graph_type in graph_types:
                    x_col, y_col = determine_columns(prompt, data.columns)
                    if x_col and y_col:
                        display_graph(data, x_col, y_col, graph_type)
                    else:
                        st.write(f"Could not determine the columns for {graph_type}.")
            else:
                st.write("No data available for the graph.")
        else:
            with st.spinner("Fetching response..."):
                ai_response = get_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            display_message("assistant", ai_response)

def fetch_data_for_graph(prompt, db):
    table_names = db.get_table_names()
    # Allow for multiple table selections in the prompt
    selected_tables = [table for table in table_names if table in prompt]

    if not selected_tables:
        st.error("No valid table name found in the prompt.")
        return None

    # Fetch data from all selected tables
    dataframes = []
    row_limit = None
    if "first" in prompt.lower():
        match = re.search(r"first (\d+)", prompt.lower())
        if match:
            row_limit = int(match.group(1))

    for table in selected_tables:
        query = f"SELECT * FROM {table}"
        if row_limit:
            query += f" LIMIT {row_limit}"

        try:
            with db._engine.connect() as conn:
                result = conn.execute(text(query))
                data = result.fetchall()
            df = pd.DataFrame(data, columns=result.keys())
            dataframes.append(df)
        except Exception as e:
            st.error(f"An error occurred while fetching data from {table}: {e}")

    # Combine dataframes if multiple tables are selected
    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    return None

def process_prompt_for_graph(prompt):
    graph_types = []
    if "bar" in prompt.lower():
        graph_types.append("Bar Graph")
    if "line" in prompt.lower():
        graph_types.append("Line Graph")
    if "pie" in prompt.lower():
        graph_types.append("Pie Chart")
    if "scatter" in prompt.lower():
        graph_types.append("Scatter Plot")
    if "histogram" in prompt.lower():
        graph_types.append("Histogram")
    
    # If no specific graph type is found, default to bar graph
    if not graph_types:
        graph_types.append("Bar Graph")
        
    return graph_types

def determine_columns(prompt, available_columns):
    # Extract column names mentioned in the prompt using regex
    mentioned_columns = [col for col in available_columns if col in prompt]
    
    if len(mentioned_columns) >= 2:
        # Return the first two mentioned columns as x and y
        return mentioned_columns[0], mentioned_columns[1]
    else:
        return None, None


def display_graph(data, x_col, y_col, graph_type):
    st.subheader(f"Generated {graph_type}")

    if not data.empty:
        fig, ax = plt.subplots(figsize=(10, 6))

        if graph_type == "Bar Graph":
            bars = ax.bar(data[x_col], data[y_col], color='skyblue')
            for bar in bars:
                yval = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, yval, 
                        f'{yval}', ha='center', va='bottom', color='black')

        elif graph_type == "Line Graph":
            ax.plot(data[x_col], data[y_col], marker='o', color='skyblue')

        elif graph_type == "Pie Chart":
            ax.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%', colors=plt.cm.Paired.colors)

        elif graph_type == "Scatter Plot":
            ax.scatter(data[x_col], data[y_col], color='skyblue')

        elif graph_type == "Histogram":
            ax.hist(data[y_col], bins=10, color='skyblue', edgecolor='black')

        if graph_type != "Pie Chart":
            ax.set_xlabel(x_col, color='white')
            ax.set_ylabel(y_col, color='white')
            ax.set_title(f"{graph_type} of {y_col} vs {x_col}", color='white')

        plt.gcf().set_facecolor(color="black")
        st.pyplot(fig)
    else:
        st.write("No data available for graph generation.")

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


