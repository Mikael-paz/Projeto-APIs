import pandas as pd
import streamlit as st

st.set_page_config(
    "Banco de dados CNPJs",
    page_icon= '🏛️',
    layout="centered",
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help':'https://instagram.com/moikael',
        'About':'App desenvolvido no curso'
    }
)
st.sidebar.success("Aqui você pode vizualisar o seu banco de dados e todas as empresas adicionadas.")