import streamlit as st

def crm_chatbot(option, display_message, get_response):
    if option == "CRM Chatbot":
        st.subheader("CRM Chatbot")

        # Initialize chat history if not already done
        if "messages" not in st.session_state:
            st.session_state.messages = []
            st.session_state["query_depth"] = 0  # Initialize query depth

        # Display chat history
        for message in st.session_state.messages:
            display_message(message["role"], message["content"])

        # User input
        if prompt := st.chat_input("Ask a question from the database ..."):
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
