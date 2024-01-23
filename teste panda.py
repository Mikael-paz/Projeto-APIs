import pandas as pd

df = pd.DataFrame({'Nome':[] , 'Data de criação':[], 'CNPJ':[] ,'Atividade principal':[] , 'Codigo':[]})
'''
dados = {
    'Nome':teste['nome'],
    'Data de criação': teste['abertura'],
    'CNPJ': teste['cnpj'],
    'Atividade principal': teste['atividade_principal'][0].get('text'),
    'Codigo':teste['atividade_principal'][0].get('code')
 }

df = pd.DataFrame([dados]) '''
print(df)