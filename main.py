from langchain.prompts import PromptTemplate

import streamlit as st
from groq import Groq
from constants import groq_key
from langchain_groq import ChatGroq

client=Groq(
    api_key=groq_key
)

st.set_page_config(page_title="ChefBot👨‍🍳")
st.sidebar.title('MENU BAR')
choice = st.sidebar.selectbox(' ', ('About Developer 👨‍💻', 'About the Project 📊'))
st.sidebar.image('')

if choice == 'About Developer 👨‍💻':
    st.title('About the Developer')
    st.image('https://media.licdn.com/media/AAYQAQSOAAgAAQAAAAAAAB-zrMZEDXI2T62PSuT6kpB6qg.png')
    st.text('Name: Divyanshu Mittal')
    st.text('Education: Master in AI & ML from Indian Institute of Information Technology, Lucknow🎓')
    st.markdown('[GitHub](https://github.com/d01mittal)')
    st.markdown('[Kaggle](https://www.kaggle.com/divu2001)')
    st.markdown('[LinkedIn](www.linkedin.com/in/divyanshu-mittal-4b652228a)')
    st.markdown('Email: msa23021@iiitl.ac.in')

elif choice == 'About the Project 📊':
    st.title('About the Project')
    st.image('https://wallpapers.com/images/featured/airport-w6v47yjhxcohsjgf.jpg')
    st.header('OVERVIEW:')
    st.text('A Streamlit app for generating the recipe for any dish.')
    st.text('This app makes things easy when planning to cook anything.')

input_text=st.text_input("Name the Dish")
prompt=PromptTemplate(
    input_variables=["name"],
    template="Tell me how to make the dish named {name}"
)

llm=ChatGroq(
    api_key=groq_key,
    model="llama3-70b-8192",)
chain=prompt | llm

st.write(chain.invoke(input_text).content)
