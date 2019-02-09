tabela = {"verde": 9.99, "azul": 19.99, "amarelo": 29.99, "vermelho": 39.99}

def consulta_valor():
    while True:
        cor = input("Digete a cor do produto: ").strip().lower()

        if cor in tabela:
            print(tabela[cor])
        else:
            print("nao esta na relação")

        consulta = input("Deseja fazer outra consulta? digite SIM: ").strip().lower()
        if consulta != "sim":
            break

if __name__ == '__main__':
    consulta_valor()