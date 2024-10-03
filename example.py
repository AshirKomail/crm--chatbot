

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from sqlalchemy import text

# def generate_graph(db, get_response):
#     st.subheader("Graph Generator")
    
#     # Step 1: Select table
#     table_names = db.get_table_names()
#     selected_table = st.selectbox("Select a table", table_names)

#     # Step 2: Enter number of user IDs
#     num_users = st.number_input("Enter the number of User IDs to fetch", min_value=1, value=5, step=1)

#     # Step 3: Select graph type (User selects graph type from the list)
#     graph_types = ["Bar Graph", "Line Graph", "Pie Chart", "Scatter Plot", "Histogram"]
#     selected_graph_type = st.selectbox("Select a graph type", graph_types)

#     # Step 4: Generate the graph once all options are selected and the button is clicked
#     if st.button("Generate Graph"):
#         # Step 5: Generate SQL Query to get user data
#         query = f"SELECT * FROM {selected_table} LIMIT :num_users"
#         try:
#             with db._engine.connect() as conn:
#                 result = conn.execute(text(query), {"num_users": num_users})
#                 data = result.fetchall()

#             # Step 6: Convert data into a Pandas DataFrame for easier handling
#             df = pd.DataFrame(data, columns=result.keys())

#             if df.empty:
#                 st.write(f"No data found in {selected_table}")
#             else:
#                 st.write(f"Data from {selected_table}:", df)

#                 # Step 7: Select the columns for plotting
#                 if 'id' in df.columns and len(df.columns) > 1:
#                     x_col = 'id'
#                     y_col = st.selectbox("Select the column for Y-axis", df.columns[1:])

#                     plt.figure(figsize=(10, 6))

#                     # Generate the graph based on the user's selection
#                     if selected_graph_type == "Bar Graph":
#                         plt.bar(df[x_col], df[y_col], color='skyblue')
#                         plt.xlabel("User ID")
#                         plt.ylabel(y_col)
#                         plt.title(f"Bar Graph of {y_col} vs User ID from {selected_table}")

#                     elif selected_graph_type == "Line Graph":
#                         plt.plot(df[x_col], df[y_col], marker='o', color='skyblue')
#                         plt.xlabel("User ID")
#                         plt.ylabel(y_col)
#                         plt.title(f"Line Graph of {y_col} vs User ID from {selected_table}")

#                     elif selected_graph_type == "Pie Chart":
#                         plt.pie(df[y_col], labels=df[x_col], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
#                         plt.title(f"Pie Chart of {y_col} from {selected_table}")

#                     elif selected_graph_type == "Scatter Plot":
#                         plt.scatter(df[x_col], df[y_col], color='skyblue')
#                         plt.xlabel("User ID")
#                         plt.ylabel(y_col)
#                         plt.title(f"Scatter Plot of {y_col} vs User ID from {selected_table}")

#                     elif selected_graph_type == "Histogram":
#                         plt.hist(df[y_col], bins=10, color='skyblue', edgecolor='black')
#                         plt.xlabel(y_col)
#                         plt.ylabel("Frequency")
#                         plt.title(f"Histogram of {y_col} from {selected_table}")

#                     st.pyplot(plt.gcf())
#                 else:
#                     st.write("The selected table doesn't have enough numeric data for graphing.")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")






# graph.py

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from sqlalchemy import text

# def generate_graph(db, get_response):
#     st.subheader("Graph Generator")
    
#     # Step 1: Select table
#     table_names = db.get_table_names()
#     selected_table = st.selectbox("Select a table", table_names)

#     # Step 2: Enter number of user IDs
#     num_users = st.number_input("Enter the number of User IDs to fetch", min_value=1, value=5, step=1)

#     # Step 3: Select graph type (User selects graph type from the list)
#     graph_types = ["Bar Graph", "Line Graph", "Pie Chart", "Scatter Plot", "Histogram"]
#     selected_graph_type = st.selectbox("Select a graph type", graph_types)

#     # Step 4: Generate the graph once all options are selected and the button is clicked
#     if st.button("Generate Graph"):
#         # Step 5: Generate SQL Query to get user data
#         query = f"SELECT * FROM {selected_table} LIMIT :num_users"
#         try:
#             with db._engine.connect() as conn:
#                 result = conn.execute(text(query), {"num_users": num_users})
#                 data = result.fetchall()

#             # Step 6: Convert data into a Pandas DataFrame for easier handling
#             df = pd.DataFrame(data, columns=result.keys())

#             if df.empty:
#                 st.write(f"No data found in {selected_table}")
#             else:
#                 st.write(f"Data from {selected_table}:", df)

#                 # Step 7: Select the columns for plotting
#                 if 'id' in df.columns and len(df.columns) > 1:
#                     x_col = 'id'
#                     y_col = st.selectbox("Select the column for Y-axis", df.columns[1:])

#                     plt.figure(figsize=(10, 6))

#                     # Set black background for the figure and axes
#                     plt.style.use('dark_background')
#                     ax = plt.gca()  # Get current axis
#                     ax.set_facecolor("black")  # Set axes background color

#                     # Generate the graph based on the user's selection
#                     if selected_graph_type == "Bar Graph":
#                         plt.bar(df[x_col], df[y_col], color='skyblue')
#                         plt.xlabel("User ID", color='white')
#                         plt.ylabel(y_col, color='white')
#                         plt.title(f"Bar Graph of {y_col} vs User ID from {selected_table}", color='white')

#                     elif selected_graph_type == "Line Graph":
#                         plt.plot(df[x_col], df[y_col], marker='o', color='skyblue')
#                         plt.xlabel("User ID", color='white')
#                         plt.ylabel(y_col, color='white')
#                         plt.title(f"Line Graph of {y_col} vs User ID from {selected_table}", color='white')

#                     elif selected_graph_type == "Pie Chart":
#                         plt.pie(df[y_col], labels=df[x_col], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
#                         plt.title(f"Pie Chart of {y_col} from {selected_table}", color='white')

#                     elif selected_graph_type == "Scatter Plot":
#                         plt.scatter(df[x_col], df[y_col], color='skyblue')
#                         plt.xlabel("User ID", color='white')
#                         plt.ylabel(y_col, color='white')
#                         plt.title(f"Scatter Plot of {y_col} vs User ID from {selected_table}", color='white')

#                     elif selected_graph_type == "Histogram":
#                         plt.hist(df[y_col], bins=10, color='skyblue', edgecolor='black')
#                         plt.xlabel(y_col, color='white')
#                         plt.ylabel("Frequency", color='white')
#                         plt.title(f"Histogram of {y_col} from {selected_table}", color='white')

#                     # Apply black background
#                     plt.gcf().set_facecolor('black')
                    
#                     st.pyplot(plt.gcf())
#                 else:
#                     st.write("The selected table doesn't have enough numeric data for graphing.")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")






# =============================================================================================

### Correct code   


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from sqlalchemy import text

# def generate_graph(db, get_response):
#     st.subheader("Graph Generator")
    
#     # Step 1: Select table
#     table_names = db.get_table_names()
#     selected_table = st.selectbox("Select a table", table_names)

#     # Step 2: Enter number of user IDs
#     num_users = st.number_input("Enter the number of User IDs to fetch", min_value=1, value=5, step=1)

#     # Step 3: Generate SQL Query to get user data
#     query = f"SELECT * FROM {selected_table} LIMIT :num_users"
#     try:
#         with db._engine.connect() as conn:
#             result = conn.execute(text(query), {"num_users": num_users})
#             data = result.fetchall()

#         # Step 4: Convert data into a Pandas DataFrame for easier handling
#         df = pd.DataFrame(data, columns=result.keys())

#         if df.empty:
#             st.write(f"No data found in {selected_table}")
#             return
#         else:
#             st.write(f"Data from {selected_table}:", df)

#             # Step 5: Select the columns for plotting
#             if 'id' in df.columns and len(df.columns) > 1:
#                 x_col = 'id'
#                 y_col = st.selectbox("Select the column for Y-axis", df.columns[1:])
#                 plt.figure(figsize=(10, 6))

#                 # Step 6: Select graph type (User selects graph type from the list)
#                 graph_types = ["Bar Graph", "Line Graph", "Pie Chart", "Scatter Plot", "Histogram"]
#                 selected_graph_type = st.selectbox("Select a graph type", graph_types)

#                 # Step 7: Generate the graph once all options are selected and the button is clicked
#                 if st.button("Generate Graph"):
#                     plt.figure(figsize=(10, 6))

#                      # Generate the graph based on the user's selection
#                     if selected_graph_type == "Bar Graph":
#                         plt.bar(df[x_col], df[y_col], color='skyblue')
#                         plt.xlabel("User ID", color='white')
#                         plt.ylabel(y_col, color='white')
#                         plt.title(f"Bar Graph of {y_col} vs User ID from {selected_table}", color='white')
                        
#                     elif selected_graph_type == "Line Graph":
#                         plt.plot(df[x_col], df[y_col], marker='o', color='skyblue')
#                         plt.xlabel("User ID", color='white')
#                         plt.ylabel(y_col, color='white')
#                         plt.title(f"Line Graph of {y_col} vs User ID from {selected_table}", color='white')

#                     elif selected_graph_type == "Pie Chart":
#                         plt.pie(df[y_col], labels=df[x_col], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
#                         plt.title(f"Pie Chart of {y_col} from {selected_table}", color='white')

#                     elif selected_graph_type == "Scatter Plot":
#                         plt.scatter(df[x_col], df[y_col], color='skyblue')
#                         plt.xlabel("User ID", color='white')
#                         plt.ylabel(y_col, color='white')
#                         plt.title(f"Scatter Plot of {y_col} vs User ID from {selected_table}", color='white')

#                     elif selected_graph_type == "Histogram":
#                         plt.hist(df[y_col], bins=10, color='skyblue', edgecolor='black')
#                         plt.xlabel(y_col, color='white')
#                         plt.ylabel("Frequency", color='white')
#                         plt.title(f"Histogram of {y_col} from {selected_table}", color='white')

#                     # Apply black background
#                     plt.gcf().set_facecolor('black')
                    
#                     st.pyplot(plt.gcf())
#                 else:
#                     st.write("The selected table doesn't have enough numeric data for graphing.")
#     except Exception as e:
#         st.error(f"An error occurred: {e}")





# ============================================================================================


# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd

# def generate_graph(db, get_response):
#     st.subheader("Graph Generator")
    
#     # Initialize chat history if not already done
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
    
#     # Display chat history
#     for message in st.session_state.messages:
#         display_message(message["role"], message["content"])

#     # User input
#     if prompt := st.chat_input("Ask for a graph from the database..."):
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})

#         # Display user message in chat
#         display_message("user", prompt)

#         # Show spinner while response is fetched
#         with st.spinner("Loading..."):
#             ai_response = get_response(prompt)

#         # Add AI response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": ai_response})

#         # Check if the user requested a graph
#         if "graph" in prompt.lower():
#             # Retrieve data for the graph from the database
#             data = fetch_data_for_graph(prompt, db)

#             # Generate and display the graph
#             if data is not None:
#                 display_graph(data)
#             else:
#                 st.write("No data available for the graph.")
#         else:
#             # Display AI text response in chat
#             display_message("assistant", ai_response)

# # Function to fetch the data for graph from the database
# def fetch_data_for_graph(prompt, db):
#     # Assuming `get_response` is structured to return the SQL result or some identifiable data
#     query_result = db.run_query(prompt)  # You can adjust this based on your DB query handling
#     if query_result:
#         df = pd.DataFrame(query_result)  # Converting the result to a DataFrame
#         return df
#     return None

# # Function to generate and display the graph
# def display_graph(data):
#     st.subheader("Generated Graph")
    
#     # Create a graph based on the returned data
#     fig, ax = plt.subplots()
    
#     if not data.empty:
#         # Here, we assume the first column is categories and the second column is values
#         data.plot(kind="bar", ax=ax)
#         st.pyplot(fig)
#     else:
#         st.write("No data available for graph generation.")

# # Function to display chat message
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

# --------------------------------------------------------------------------------




#------- just for checking code  ---------------------------


# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# from sqlalchemy import text

# def generate_graph(db, get_response):
#     st.subheader("Graph Generator")

#     # Initialize chat history if not already done
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display chat history
#     for message in st.session_state.messages:
#         display_message(message["role"], message["content"])

#     # User input
#     if prompt := st.chat_input("Ask for a graph from the database..."):
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})

#         # Display user message in chat
#         display_message("user", prompt)

#         # Check if the user requested a graph
#         if "graph" in prompt.lower():
#             with st.spinner("Loading..."):
#                 # Fetch data based on the user request
#                 data = fetch_data_for_graph(prompt, db)

#             # Generate and display the graph
#             if data is not None:
#                 display_graph(data)
#             else:
#                 st.write("No data available for the graph.")
#         else:
#             # Generate AI response if no graph is requested
#             with st.spinner("Fetching response..."):
#                 ai_response = get_response(prompt)

#             # Add AI response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": ai_response})

#             # Display AI response in chat
#             display_message("assistant", ai_response)

# def fetch_data_for_graph(prompt, db):
#     # Extract the table name based on user input (you might want to improve this parsing)
#     table_names = db.get_table_names()
    
#     # Here, we need a more sophisticated method to extract table name and any conditions from the prompt
#     # For demonstration, we assume the first found table in the prompt
#     selected_table = next((table for table in table_names if table in prompt), None)

#     if selected_table is None:
#         st.error("No valid table name found in the prompt.")
#         return None

#     # Generate a basic SQL Query (adjust this based on the actual conditions you want to support)
#     query = f"SELECT * FROM {selected_table}"

#     try:
#         with db._engine.connect() as conn:
#             result = conn.execute(text(query))
#             data = result.fetchall()

#         df = pd.DataFrame(data, columns=result.keys())
#         return df
#     except Exception as e:
#         st.error(f"An error occurred while fetching data: {e}")
#         return None


# def display_graph(data):
#     st.subheader("Generated Graph")

#     if not data.empty:
#         # Select x and y columns
#         x_col = 'id'  # Assume 'id' is the x-axis
#         y_col = st.selectbox("Select the column for Y-axis", data.columns[1:])  # Exclude x_col from options

#         # Select graph type
#         graph_types = ["Bar Graph", "Line Graph", "Pie Chart", "Scatter Plot", "Histogram"]
#         selected_graph_type = st.selectbox("Select a graph type", graph_types)

#         # Create a graph based on the user's selection
#         fig, ax = plt.subplots(figsize=(10, 6))
#         if selected_graph_type == "Bar Graph":
#             ax.bar(data[x_col], data[y_col], color='skyblue')
#         elif selected_graph_type == "Line Graph":
#             ax.plot(data[x_col], data[y_col], marker='o', color='skyblue')
#         elif selected_graph_type == "Pie Chart":
#             ax.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
#         elif selected_graph_type == "Scatter Plot":
#             ax.scatter(data[x_col], data[y_col], color='skyblue')
#         elif selected_graph_type == "Histogram":
#             ax.hist(data[y_col], bins=10, color='skyblue', edgecolor='black')

#         # Set labels and title
#         ax.set_xlabel("User ID", color='white')
#         ax.set_ylabel(y_col, color='white')
#         ax.set_title(f"{selected_graph_type} of {y_col} vs User ID", color='white')

#         # Apply black background
#         plt.gcf().set_facecolor('black')

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






#------------------------------------------------------------------------------------------




# Display graph but wrong graph but the code is correct 


# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# from sqlalchemy import text

# def generate_graph(db, get_response):
#     st.subheader("Graph Generator")

#     # Initialize chat history if not already done
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display chat history
#     for message in st.session_state.messages:
#         display_message(message["role"], message["content"])

#     # User input
#     if prompt := st.chat_input("Ask for a graph from the database..."):
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})

#         # Display user message in chat
#         display_message("user", prompt)

#         # Check if the user requested a graph
#         if "graph" in prompt.lower():
#             with st.spinner("Loading..."):
#                 # Fetch data based on the user request
#                 data = fetch_data_for_graph(prompt, db)

#             # Generate and display the graph
#             if data is not None:
#                 y_col, graph_type = process_prompt_for_graph(prompt, data.columns)
#                 if y_col and graph_type:
#                     display_graph(data, y_col, graph_type)
#                 else:
#                     st.write("Could not determine the Y-axis column or graph type from the prompt.")
#             else:
#                 st.write("No data available for the graph.")
#         else:
#             # Generate AI response if no graph is requested
#             with st.spinner("Fetching response..."):
#                 ai_response = get_response(prompt)

#             # Add AI response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": ai_response})

#             # Display AI response in chat
#             display_message("assistant", ai_response)

# def fetch_data_for_graph(prompt, db):
#     # Extract the table name based on user input
#     table_names = db.get_table_names()
#     selected_table = next((table for table in table_names if table in prompt), None)

#     if selected_table is None:
#         st.error("No valid table name found in the prompt.")
#         return None

#     query = f"SELECT * FROM {selected_table}"

#     try:
#         with db._engine.connect() as conn:
#             result = conn.execute(text(query))
#             data = result.fetchall()

#         df = pd.DataFrame(data, columns=result.keys())
#         return df
#     except Exception as e:
#         st.error(f"An error occurred while fetching data: {e}")
#         return None

# def process_prompt_for_graph(prompt, columns):
#     # Logic to extract Y-axis column and graph type from prompt
#     # Here, we use a simple heuristic to identify keywords for graph type
#     graph_types = ["Bar Graph", "Line Graph", "Pie Chart", "Scatter Plot", "Histogram"]
    
#     # Default values
#     y_col = None
#     graph_type = None

#     # Simple heuristics (this can be improved with NLP techniques)
#     for col in columns:
#         if col.lower() in prompt.lower():
#             y_col = col
#             break

#     for g_type in graph_types:
#         if g_type.lower() in prompt.lower():
#             graph_type = g_type
#             break

#     return y_col, graph_type

# def display_graph(data, y_col, graph_type):
#     st.subheader("Generated Graph")

#     if not data.empty:
#         x_col = 'id'  # Assume 'id' is the x-axis

#         # Create a graph based on the user's selection
#         fig, ax = plt.subplots(figsize=(10, 6))
#         if graph_type == "Bar Graph":
#             ax.bar(data[x_col], data[y_col], color='skyblue')
#         elif graph_type == "Line Graph":
#             ax.plot(data[x_col], data[y_col], marker='o', color='skyblue')
#         elif graph_type == "Pie Chart":
#             ax.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
#         elif graph_type == "Scatter Plot":
#             ax.scatter(data[x_col], data[y_col], color='skyblue')
#         elif graph_type == "Histogram":
#             ax.hist(data[y_col], bins=10, color='skyblue', edgecolor='black')

#         # Set labels and title
#         ax.set_xlabel("User ID", color='white')
#         ax.set_ylabel(y_col, color='white')
#         ax.set_title(f"{graph_type} of {y_col} vs User ID", color='white')

#         # Apply black background
#         plt.gcf().set_facecolor('black')

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



# ----------------------------------------------------------------------------------------
# Display graph with correct bar graph and also the code is correct 


# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# from sqlalchemy import text
# import re

# def generate_graph(db, get_response):
#     st.subheader("Graph Generator")

#     # Initialize chat history if not already done
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display chat history
#     for message in st.session_state.messages:
#         display_message(message["role"], message["content"])

#     # User input
#     if prompt := st.chat_input("Ask for a graph from the database..."):
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})

#         # Display user message in chat
#         display_message("user", prompt)

#         # Check if the user requested a graph
#         if "graph" in prompt.lower():
#             with st.spinner("Loading..."):
#                 # Fetch data based on the user request
#                 data = fetch_data_for_graph(prompt, db)

#             # Generate and display the graph
#             if data is not None:
#                 x_col, y_col, graph_type = process_prompt_for_graph(prompt, data.columns)
#                 if x_col and y_col and graph_type:
#                     display_graph(data, x_col, y_col, graph_type)
#                 else:
#                     st.write("Could not determine the columns or graph type from the prompt. Defaulting to 'id' for X-axis and auto-selected Y-axis.")
#                     y_col = data.columns[1] if len(data.columns) > 1 else 'id'
#                     display_graph(data, 'id', y_col, 'Bar Graph')  # Fallback to bar graph
#             else:
#                 st.write("No data available for the graph.")
#         else:
#             # Generate AI response if no graph is requested
#             with st.spinner("Fetching response..."):
#                 ai_response = get_response(prompt)

#             # Add AI response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": ai_response})

#             # Display AI response in chat
#             display_message("assistant", ai_response)

# def fetch_data_for_graph(prompt, db):
#     # Extract the table name based on user input
#     table_names = db.get_table_names()
#     selected_table = next((table for table in table_names if table in prompt), None)

#     if selected_table is None:
#         st.error("No valid table name found in the prompt.")
#         return None

#     # Parse row limit from prompt (default to None if not specified)
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

# def process_prompt_for_graph(prompt, columns):
#     # Default columns
#     x_col = None
#     y_col = None
#     graph_type = None

#     # Look for specific column requests
#     if "id" in prompt.lower():
#         x_col = 'id'
#     if "campaign_id" in prompt.lower():
#         y_col = 'campaign_id'

#     # Determine graph type (default to bar graph if not mentioned)
#     graph_type = "Bar Graph"
    
#     return x_col, y_col, graph_type


# def display_graph(data, x_col, y_col, graph_type):
#     st.subheader(f"Generated {graph_type}")

#     if not data.empty:
#         # Create a graph based on the user's selection
#         fig, ax = plt.subplots(figsize=(10, 6))

#         if graph_type == "Bar Graph":
#             bars = ax.bar(data[x_col], data[y_col], color='skyblue')

#             # Add y-axis values on top of the bars
#             for bar in bars:
#                 yval = bar.get_height()
#                 ax.text(bar.get_x() + bar.get_width() / 2, yval, 
#                         f'{yval}', ha='center', va='bottom', color='black')

#         elif graph_type == "Line Graph":
#             lines = ax.plot(data[x_col], data[y_col], marker='o', color='skyblue')


#         elif graph_type == "Pie Chart":
#             ax.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%', colors=plt.cm.Paired.colors)

#         elif graph_type == "Scatter Plot":
#             ax.scatter(data[x_col], data[y_col], color='skyblue')

#         elif graph_type == "Histogram":
#             ax.hist(data[y_col], bins=10, color='skyblue', edgecolor='black')

#         # Set labels and title for all graphs except Pie Chart
#         if graph_type != "Pie Chart":
#             ax.set_xlabel(x_col, color='white')
#             ax.set_ylabel(y_col, color='white')
#             ax.set_title(f"{graph_type} of {y_col} vs {x_col}", color='white')

#         # Apply black background
#         plt.gcf().set_facecolor('black')

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

