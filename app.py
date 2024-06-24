# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image



os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
   
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Smart Translator")

## idioms and phrases translator
st.header("Idioms and Phrases Translator")
prewritten_text = "Explain this idioms in English and Hindi "

input=st.text_input("Enter any Idioms and Phrases: ")

combined_text =f"{prewritten_text}  ,{input}"

submit=st.button("Translate Idioms")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(combined_text)
    st.subheader("The meaning of Idioms is:")
    st.write(response)

## Hindi Translator 
st.header("Hindi Translator")

text="Translate into Hindi"

engInput=st.text_input("Enter your text : ")

comtext=f"{text},{engInput}"

submitbtn=st.button("Translate Text")

if submitbtn:
    
    response=get_gemini_response(comtext)
    st.subheader("The Response is")
    st.write(response)

## image translator 
model = genai.GenerativeModel('gemini-pro-vision')
textinp="Translate into Hindi"
def get_gemini_response(textinp,image):
    
    if textinp!="":
       response = model.generate_content([textinp,image])
    else:
       response = model.generate_content(image)
    return response.text

st.header("Image Translator ")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(textinp,image)
    st.subheader("The Response is")
    st.write(response)

