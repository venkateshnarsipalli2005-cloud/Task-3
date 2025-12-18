import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Ensure the NLTK 'punkt' tokenizer is available (used by word_tokenize).
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

st.title("🤖 Customer Support Chatbot")

# 1. Load the Knowledge Base
try:
    df = pd.read_csv("sample_faq.csv")
    # Clean column names to handle spaces
    df.columns = [c.strip().lower() for c in df.columns]
    
    st.success("✅ Knowledge Base Loaded!")
    
    # Show the questions so you know what to ask
    with st.expander("Show me what I can ask"):
        st.table(df[['question', 'answer']])

except FileNotFoundError:
    st.error("Error: 'sample_faq.csv' not found. Please check your folder.")
    st.stop()

# 2. User Input
user_input = st.text_input("Type your question here (e.g., 'Where is my order?'):")

# 3. The "Brain" (Rule-Based Matching)
if user_input:
    # Break user input into a set of words
    user_tokens = set(word_tokenize(user_input.lower()))
    found_answer = False
    
    for index, row in df.iterrows():
        question = str(row['question'])
        answer = str(row['answer'])
        
        # Check for simple greetings
        if user_input.lower() in ['hi', 'hello', 'hey']:
            if 'hi' in question.lower() or 'hello' in question.lower():
                st.write(f"**Bot:** {answer}")
                found_answer = True
                break

        # Check for matching words
        question_tokens = set(word_tokenize(question.lower()))
        common_words = user_tokens.intersection(question_tokens)
        
        # If there is at least 1 meaningful word in common, give the answer
        if len(common_words) >= 1:
            st.write(f"**Bot:** {answer}")
            found_answer = True
            break
            
    if not found_answer:
        st.warning("I don't know the answer to that yet. Try picking a question from the list above!")