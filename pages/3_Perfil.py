import streamlit as st
import requests

st.set_page_config(page_title="Rahná Cadastro",page_icon="🐶")

st.write("# Cadastre seu dog!🐶")

with st.form("my_form"):
    name = st.text_input("Nome do dog: 👇", max_chars = 20)
    age = st.number_input("Idade do dog: 👇", min_value=0, max_value=25)
    weight = st.number_input("Peso do dog: 👇", min_value=0, max_value=50)
    parent = st.text_input("Nome do responsável pelo dog: 👇", max_chars = 40)
    phone = st.text_input("Telefone do responsável pelo dog: 👇", max_chars = 20)
    email = st.text_input("Email do responsável pelo dog: 👇", max_chars = 40)

    submitted = st.form_submit_button("Submit")

    if submitted:
        data= {'name' : name,
        'age' : age,
        'weight' : weight,
        'parent_name' : parent,
        'phone' : phone,
        'email' : email}

        url = "http://localhost:5000/add-dog"
        response = requests.post(url, json= data)
