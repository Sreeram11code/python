import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title = "PYTHON", page_icon = "🎉")
tabs = st.tabs(["INTRODUCTION", "PERSONAL DETAILS", "ABOUT", "DATA"])
with tabs[0]:
    st.title("FACTS ABOUT PYTHON:❤...")
    st.subheader("Hi! This is Sreeram👋! LET'S SEE ABOUT PYTHON...")
    st.title("INTRODUCTION😎 AND HOBBIES:")
    st.write("I am Sreeram! And my hobbies are playing badminton and computer programming (Python). I also have a youtube channel.. pls subscribe!")
    st.write("This website was created by using PYTHON...")
    st.write("[CODE >](https://trinket.io/python/3e8f14f96a)")
    st.write("[YouTube >](https://www.youtube.com/@WELLBITES-yo8hp)")
    st.write("__________________________________________________________________")
with tabs[1]:
    st.subheader("PERSONAL INFORMATON:")
    name = st.text_input("Enter your name:")
    age = st.text_input("Enter your age:")
    if age and name is not None:
        st.write("Thank You! For updating your personal details!")
        st.write("_______________________________________________________________________")
with tabs[2]:
    if age and name is not None:
        st.title("ABOUT PYTHON:")
        st.subheader("KEY POINTS:")
        st.write("•Python is designed to be easy to read and write.This makes it beginner-friendly.")
        st.write("•Python code is executed line by line, which allows for immediate feedback and makes debugging easier.")
        st.write("•Variables in Python do not require explicit declaration of data types, as the interpreter infers the type at runtime.")
        st.write("•Python comes with a vast standard library that provides modules andfunctions for various tasks, from file I/O to web development.")
        st.write("•Python can run on different operating systems, including Windows, macOS, and Linux, without requiring modifications to the code.")
        st.write("•Python has a large ecosystem of third-party libraries and frameworks, such as NumPy for numerical computations, Pandas for data analysis, Django for web development, and TensorFlow for machine learning.")
        st.write("_______________________________________________________________________")
with tabs[3]:
    uploaded_file = st.file_uploader("Upload your CSV file:", type = "csv")
    if uploaded_file is not None:
        st.write("Successfully Uploaded👏...")
        st.balloons()
        df = pd.read_csv(uploaded_file)
        st.write("_______________________________________________________________________")
        st.subheader("DATA PREVIEW:")
        st.write(df.head())
        st.write("_______________________________________________________________________")
        st.subheader("DATA SUMMEARY:")
        st.write(df.describe())
        st.write("_______________________________________________________________________")
        st.subheader("FILTER DATA:")
        columns = df.columns.to_list()
        selected_column = st.selectbox("Select column to filter by:", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select Value:", unique_values)
        filtered_df = df[df[selected_column] ==  selected_value]
        st.write(filtered_df)
        st.write("_______________________________________________________________________")
        st.subheader("PLOT DATA:")
        x_axis = st.selectbox("Select x-axis column", columns)
        y_axis = st.selectbox("Select y-axis column", columns)
        if st.button("Generate Plot:"):
            st.line_chart(filtered_df.set_index(x_axis)[y_axis])
            st.write("_______________________________________________________________________")
        else:
            st.write("ignore")
    else:
        st.write("Waiting to upload file...")