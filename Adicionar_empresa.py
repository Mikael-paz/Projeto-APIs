import requests
import json
import pandas as pd
import streamlit as st

# Função Do API
token = "d189bdc8986a538daa5d4ddee5246b0542b2be3919c5fcd42434fe6982d5f599"
#cnpj = '52924566000103'
def apireceita(token,cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":token,"cnpj":cnpj,"plugin":"RF"}
    response = requests.request("GET", url, params=querystring)
    resp = json.loads(response.text)
    return resp

# Configuração da página (Streamlit)
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
st.sidebar.success("Aqui você pode adicionar uma empresa nova no seu banco de dados"
                   "Busque a empresa que quer adicionar na nuvem atraves da API ou então digite manualmente.")
col1,col2,col3 = st.columns([1,10,1], gap = 'small')

# Formulario principal
with col2:
#Buscar
    st.title('Adicionar uma empresa nova')
    st.subheader('Buscar empresa')
    cnpj= st.text_input('CNPJ:',max_chars=14, key='cnpjbuscar')
    if st.button('Buscar na API',key='buscar'): 
        teste = apireceita(token,cnpj)
        print(cnpj)

#Manual
    st.write('---')
    st.subheader('Digitar manualmente')
    st.text_input('Nome: ')
    st.text_input('Data de Criação')
    st.text_input('CNPJ: ')
    st.text_input('Atividade Principal')
    st.text_input('Codigo da Atividade')
    st.button('Adicionar')


df = pd.DataFrame({'Nome':[] , 'Data de criação':[] , 'CNPJ':[] ,'Atividade principal':[] , 'Codigo':[]})

#dados = {
#    'Nome':teste['nome'],
#    'Data de criação': teste['abertura'],
#    'CNPJ': teste['cnpj'],
#    'Atividade principal': teste['atividade_principal'][0].get('text'),
#    'Codigo':teste['atividade_principal'][0].get('code')
# }
#df = pd.DataFrame([dados]) 

