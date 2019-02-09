import requests
import json
import pandas as pd

response = requests.get("http://dadosabertos.ibama.gov.br/dados/SICAFI/AC/Quantidade/multasDistribuidasBensTutelados.json")
if response.status_code == 200:
    print("Êxito na conexão...")
    lista_json = response.json()
    informações = len(lista_json["data"])
    print("foram encontrados %s informações" % informações)
    lista_dataAuto = []
    lista_cidade = []
    lista_nomeRazaoSocial = []
    lista_tipoInfracao = []
    lista_valorAuto = []
    lista_situcaoDebito = []
    anos_80 = ["1980", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989"]
    print(anos_80)
