import streamlit as st
import pandas as pd
import numpy as np
import easyocr

selectbox1 = st.sidebar.selectbox("Demo Page 1",["word app","image app"])

if selectbox1 == "word app":
    st.title('Text Analysis')
    user_input = st.text_input("Enter the text:",key='input')
    #Button
    if st.button('submit'):
        n_words = len(user_input.split())
        st.write('Number of words in the text: ', str(n_words))

if selectbox1 == "image app":
    st.title('Image Analysis')
    file = st.file_uploader("Please upload an image", type=["png","jpg","jpeg"])
    if file:
        filename = file.name
        with open(filename, mode='wb') as f: 
            f.write(file.read())
        #Container
        images = st.container()
        with images:
            _left,_mid,_right = st.columns([1, 1, 1])
        with _left:
            st.subheader('Uploaded Image')
            st.image(filename)
        #Text from Image.
        reader = easyocr.Reader(['en'])
        result = reader.readtext(filename)
        text = result[0][1]

        with _right:
            st.subheader('Text Detected')
            st.write('Detected Text: ', text)


