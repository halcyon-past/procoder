import os
import openai
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Retrieve the password from the environment variable
PASSWORD = os.getenv("PASSWORD")
if not PASSWORD:
    raise ValueError("PASSWORD is not set in the .env file.")

# Initialize OpenAI client with Azure-specific URL and API key
client = openai.OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("OPENAI_API_KEY"),
)

def get_ai_response(conversation, model):
    """Generates a response from the AI model based on the conversation history."""
    try:
        response = client.chat.completions.create(
            messages=conversation,
            model=model
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, I couldn't process that request due to an error."

# Streamlit app configuration and title
st.set_page_config(page_title="Procoder", page_icon="🤖", layout="wide")

# Password authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Password Protected App")
    password_input = st.text_input("Enter Password:", type="password")
    if st.button("Login"):
        if password_input == PASSWORD:
            st.session_state.authenticated = True
            st.success("Access granted! Welcome to ProCoder.")
        else:
            st.error("Incorrect password. Please try again.")
else:
    st.title("💬 ProCoder")

    # Model selection dropdown
    model_options = ["gpt-4o", "gpt-4o-mini", "o1-mini", "o1-preview", "o1"]
    selected_model = st.selectbox("Choose AI Model", model_options, index=0)

    # Initialize session state for conversation
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # Display chat messages
    for msg in st.session_state.conversation:
        role = "user" if msg["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.markdown(msg["content"])

    # User input for chat
    if prompt := st.chat_input("Type your message here..."):
        # Append user input to conversation
        st.session_state.conversation.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display AI response
        with st.chat_message("assistant"):
            with st.spinner("ProCoder is typing..."):
                ai_response = get_ai_response(st.session_state.conversation, selected_model)
                st.markdown(ai_response)
                st.session_state.conversation.append({"role": "assistant", "content": ai_response})

    # Footer with social links
    st.markdown("---")
    st.markdown(
        """
        <style>
            .footer { text-align: center; font-size: 0.9em; color: #888; margin-top: 2em; }
            .footer a { color: #4C8BF5; text-decoration: none; }
        </style>
        <div class="footer">
            Made with ❤️ by Aritro Saha <br>
            <a href="https://github.com/halcyon-past" target="_blank">GitHub</a> | 
            <a href="https://www.linkedin.com/in/aritro-saha/" target="_blank">LinkedIn</a> | 
            <a href="https://aritro.tech/" target="_blank">Portfolio</a>
        </div>
        """,
        unsafe_allow_html=True
    )
