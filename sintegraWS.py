import requests
import json

def apireceita(token,cnpj):
    url = "https://www.sintegraws.com.br/api/v1/execute-api.php"

    querystring = {"token":token,"cnpj":cnpj,"plugin":"RF"}

    response = requests.request("GET", url, params=querystring)
    print(response)
    resp = json.loads(response.text)
    return resp

token = "6858C82C-19CE-43C1-80FF-97722C6F31C3"
cnpj = '52924566000103'

teste = apireceita(token,cnpj)
print(teste)
print(teste['nome'])
print(teste['telefone'])