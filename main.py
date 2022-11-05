import streamlit as st
import Controllers.ClienteController as ClienteController
import models.cliente as cliente

st.title("Incluir Cliente")

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
    input_occupation = st.selectbox("Selecione sua profissão", ["", "Desenvolvedor", "Músico", "Designer", "Professor"])
    input_button_submit = st.form_submit_button("Enviar")

if input_button_submit:
    cliente.nome = input_name
    cliente.idade = input_age
    cliente.profissao = input_occupation

    ClienteController.Incluir(cliente)
    st.success("Cliente incluido com sucesso!")