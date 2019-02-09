                            # Taxa de conversão cambial

import requests                                                 # requisição de sites
import jsons                                                    # importação de informação (arquivo) de um sistema e transfeirr para outro

def principal():                                                     # criar uma função MAIN para chamar as funções criadas abaixo
    print("Estabelecendo conexão com o link... ")               # MAIN é a primeira função a ser executada.
    response = requests.get("http://data.fixer.io/api/latest?access_key=d5b76e6657d7268f23eb5048604dcfad&format=1")
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()                                      # pega o json do site na variavel response
        att = dados["date"]
        split = att.split("-")
        print("atualizado em : %s/%s/%s" % (split[2], split[1], split[0]))
        cambio_dollar(dados)
        cambio_euro(dados)
    else:
        print("Site com algum problema...")

def cambio_dollar(d):                                            # criação de função para utilizar em outros programas
    taxa_usd = d['rates']['USD']                                 # utilizando uma variavel dentro da função para poder rodar
    taxa_brl = d['rates']['BRL']
    real = taxa_brl / taxa_usd
    print("1 Dollar equivale a %.2f Reais" % real)

def cambio_euro(d):
    taxa_eur = d['rates']['EUR']
    taxa_brl = d['rates']['BRL']
    real2 = taxa_brl / taxa_eur
    print("1 Euro equivale a %.2f Reais" % real2)

# Pede para que o programa execute a nossa função MAIN
if __name__ == '__main__':
    principal()