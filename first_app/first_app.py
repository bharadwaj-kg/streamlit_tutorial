import streamlit as st

st.title('Text Analysis')

user_input = st.text_input("Enter the text:",key='input')

if user_input:
    n_words = len(user_input.split())
    st.write('Number of words in the text: ', str(n_words))