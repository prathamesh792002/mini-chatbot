import streamlit as st
from model import load_model, generate_response

# Load the model and tokenizer
model, tokenizer = load_model()

# Streamlit app layout
st.set_page_config(page_title="ChatGPT Mini", page_icon=":robot_face:")

st.title("ChatGPT Mini")
st.write("A mini version of ChatGPT for your final year project!")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        response = generate_response(model, tokenizer, user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))
    else:
        st.warning("Please enter a message.")

# Display chat history
for sender, message in st.session_state.history:
    st.markdown(f"**{sender}:** {message}")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.history = []
