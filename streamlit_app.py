import streamlit as st
import os
from PIL import Image #pillow library is for image handling
import google.generativeai as genai

genai.configure(api_key = "AIzaSyAVtthYPL9eOGa1g6vmPccuIpzb3W8HVf8")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt]) #model has an inbuilt function c/d generate_content
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
            "mime_type": uploaded_file.type,
            "data": bytes_data
            }
        ]
        return image_parts
    else: 
        raise FileNotFoundError("No file was uploaded. Please upload file.")

st.set_page_config(page_title="Invoive Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Medha Goel")
st.sidebar.write("Powered by google gemini ai")
st.header("RoboBill")
st.subheader("Made by Medha Goel")
st.subheader("Manage your expense with RoboBill")
input = st.text_input("What do you want me to do ?",key="input")
uploaded_file = st.file_uploader("Choose an image", type=['jpg','jpeg','png'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width="True")

submit = st.button("Let's Go!")

input_prompt = """
You are an expert in reading  invoices. We are going to upload an image of a bill and you will have to answer any type of questions that the user asks you. You have to greet the user first. Make sure to keep the fonts uniform and give the items list in a point-wise format.
At the end, make sure to repeat the name of our app "RoboBill" and ask the user to use it again.
""" 
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data,input)
    st.subheader("Here's what you need to know:")
    st.write(response)

