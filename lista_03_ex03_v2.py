lados_triangulo = []

def classificacao():
    giro = True
    while giro:
        i = 0
        while i < 3:
            try:
                lado = int(input("Insira a medida: "))
                lados_triangulo.append(lado)
                i = i + 1
            except:
                print("Insira apenas numero!")


        sobra = set(lados_triangulo)
        setado = len(sobra)

        if setado == 3:
            print("Escaleno")
        elif setado == 2:
            print("Isósceles")
        elif setado == 1:
            print("Equilátero")
        lados_triangulo.clear()

        r = input("Deseja repetir: SIM ou NAO?").strip().upper()
        if r == "SIM":
            giro = True
        else:
            giro = False

if __name__ == '__main__':
    classificacao()
