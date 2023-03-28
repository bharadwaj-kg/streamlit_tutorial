import streamlit as st
import pandas as pd
import numpy as np
import cv2

radio1 = st.sidebar.radio("Demo Page 2",["video app", "plot app"])

if radio1 == "video app":
    st.title('Video Analysis')
    file = st.file_uploader("Please upload a video", type=["mp4"])
    if file:
        filename = file.name
        with open(filename, mode='wb') as f: 
            f.write(file.read())
        #Container
        videos = st.container()
        with videos:
            _left,_right = st.columns([1, 2])
        with _left:
            st.subheader('Uploaded Video')
            st.video(filename)
        #Number of frames from video.
        vid = cv2.VideoCapture(filename)
        # count the number of frames
        frames = vid.get(cv2.CAP_PROP_FRAME_COUNT)

        with _right:
            st.subheader('Number of Frames')
            st.write('Number of Frames in the video: ', str(frames))

if radio1 == "plot app":
    st.title('Data and Plots')
    df = pd.DataFrame(np.random.randn(5, 3),columns=['l1', 'l2', 'l3'])
    st.subheader('Data')
    st.dataframe(df)
    st.subheader('Plot')
    st.line_chart(df)


