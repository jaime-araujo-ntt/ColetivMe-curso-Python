

lista_dados = [5, 7, 11, 23, 0]
lista_nova = []

i = 0
while i < 5:
    try:
        if i < 1:
            num = int(input("insira o numero: "))
            i += 1
            lista_nova.append(num)
        else:
            num = int(input("insira outro numero: "))
            lista_nova.append(num)
            i += 1
    except:
        print("insira apenas numeros!")

for novo in lista_nova:
    if novo not in lista_dados:
        lista_dados.append(novo)
print(lista_dados)

