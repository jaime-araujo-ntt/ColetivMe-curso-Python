lados = []
quantidade = 3

while quantidade > 0:
    lado = int(input("Informe um lado do triângulo: "))
    lados.append(lado)
    quantidade = quantidade - 1

lados = set(lados)  #elimina dados repetidos, consevando apenas 1
diferentes = len(lados)

if diferentes == 1:
    print("Equilátero")
elif diferentes == 2:
    print("Isósceles")
elif diferentes == 3:
    print("Escaleno")
