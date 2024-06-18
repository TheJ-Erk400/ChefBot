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
choice = st.sidebar.selectbox(' ', ('About Developer 👨‍💻'))
st.sidebar.image('https://www.google.com/imgres?q=chole%20bhature%20image&imgurl=https%3A%2F%2Fstatic.toiimg.com%2Fphoto%2F98230357.cms&imgrefurl=https%3A%2F%2Ftimesofindia.indiatimes.com%2Flife-style%2Ffood-news%2Fthis-is-how-chole-bhatura-came-to-india%2Fphotostory%2F98230348.cms&docid=u54M5ugLzhGQYM&tbnid=QmgOApTDYCG5iM&vet=12ahUKEwid-47UseWGAxUsZ_UHHVLcD10QM3oECHsQAA..i&w=1200&h=900&hcb=2&ved=2ahUKEwid-47UseWGAxUsZ_UHHVLcD10QM3oECHsQAA')

if choice == 'About Developer 👨‍💻':
    st.title('About the Developer')
    st.image('https://media.licdn.com/media/AAYQAQSOAAgAAQAAAAAAAB-zrMZEDXI2T62PSuT6kpB6qg.png')
    st.text('Name: Divyanshu Mittal')
    st.text('Education: Master in AI & ML from Indian Institute of Information Technology, Lucknow🎓')
    st.markdown('[GitHub](https://github.com/d01mittal)')
    st.markdown('[Kaggle](https://www.kaggle.com/divu2001)')
    st.markdown('[LinkedIn](www.linkedin.com/in/divyanshu-mittal-4b652228a)')
    st.markdown('Email: msa23021@iiitl.ac.in')

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
