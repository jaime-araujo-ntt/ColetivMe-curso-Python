from termcolor import cprint
lados_triangulo = []

def tipos_triangulo():
    r = True
    while r:
        i = 0
        while i < 3:
            try:
                l = int(input("Insira o tamanho do lado: "))
                lados_triangulo.append(l)
                i = i + 1
            except:
                print("Insira apenas numeros!")

        if lados_triangulo[0] == lados_triangulo[1] and lados_triangulo[0] == lados_triangulo[2]:
            cprint("equilatero", "blue")
        elif lados_triangulo[0] == lados_triangulo[1] and lados_triangulo[0] != lados_triangulo[2]:
            cprint("isósceles", "red")
        elif lados_triangulo[0] == lados_triangulo[2] and lados_triangulo[0] != lados_triangulo[1]:
            cprint("isósceles", "red")
        elif lados_triangulo[0] == lados_triangulo[2] and lados_triangulo[1] != lados_triangulo[0]:
            cprint("isósceles", "red")
        elif lados_triangulo[0] != lados_triangulo[1] and lados_triangulo[1] != lados_triangulo[2]:
            cprint("escaleno", "yellow")
        else:
            print("ERRO NO PROGRAMA!")
        lados_triangulo.clear()

        repetir = input("digite SIM para novas comparações: ").strip().upper()
        if repetir == "SIM":
            r = True
        else:
            r = False

if __name__ == '__main__':
    tipos_triangulo()