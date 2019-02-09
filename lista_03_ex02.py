from termcolor import cprint

preco = [9.99, 19.99, 29.99, 39.99]
cor = ["verde", "azul", "amarelo", "vermelho"]

def consulta_valor():

    repetir = True
    while repetir:
        while True:
            pedido = input("Qual a COR do CD escolhido: ").strip().lower()
            if pedido == "verde":
                cprint(preco[0], 'green')
                break
            elif pedido == "azul":
                cprint(preco[1], "blue")
                break
            elif pedido == "amarelo":
                cprint(preco[2], "yellow")
                break
            elif pedido == "vermelho":
                cprint(preco[3], "red")
                break
            else:
                print("Não está na relação")
        r = input("deseja consultar novamente? digite SIM: ").lower().strip()
        if r == "sim":
            repetir = True
        else:
            repetir = False

if __name__ == '__main__':
    consulta_valor()
