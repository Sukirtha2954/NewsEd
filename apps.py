import streamlit as st
from transformers import pipeline

# Load T5 model
model = pipeline("text2text-generation", model="t5-small")

# Streamlit UI with ChatGPT-like layout
st.set_page_config(page_title="Chat Interface", layout="wide")
st.markdown("<h1 style='text-align: center;'>Query Based Model - Decoder</h1>", unsafe_allow_html=True)

# Predefined Context
context = (
    "The Expanded Programme on Immunisation was launched by the WHO in 1974. "
    "Smallpox was declared eradicated in 1980 after a successful global vaccination campaign. "
    "The climate crisis is spurring disease outbreaks in vulnerable communities. "
    "The UK is considering a significant cut to its support for global vaccine programs. "
    "Polio remains endemic in just a few countries, but progress is steady."
)
st.write("### Context:")
st.write(context)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat display area
chat_container = st.container()

# Display chat history with alternating user and bot messages
with chat_container:
    for query, answer in st.session_state.chat_history:
        st.markdown(f"""
        <div style='text-align: left; background-color: #e7f3fe; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>
            <b>You:</b><br>{query}
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div style='text-align: left; background-color: #f3e7fe; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>
            <b>Bot:</b><br>{answer}
        </div>
        """, unsafe_allow_html=True)

# Input area fixed at the bottom
st.write("### Enter your query below:")
user_question = st.text_input("", key="user_input")

if st.button("Get Answer") and user_question:
    input_text = f"question: {user_question} context: {context}"
    response = model(input_text, max_length=50, do_sample=False)[0]['generated_text']
    
    # Store query and response
    st.session_state.chat_history.append((user_question, response))
    st.rerun()
