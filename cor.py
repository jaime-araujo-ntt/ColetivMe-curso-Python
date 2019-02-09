lista = ["rosa", "amarelo", "azul", "amarelo"]
tamanho = len(lista)
i = 0

# percorrendo lista
while i < tamanho:
    if lista[i] == "amarelo":
        print("A posição na lista é {}".format(i))
    i += 1

# percorrendo lista
for cor in lista:
    print(cor)

# inserindo na lista
print("------Inserindo na lista------")
lista.append("preto")
for cor in lista:
    print(cor)

# removendo da lista
print("------Removendo na lista------")
lista.pop()
for cor in lista:
    print(cor)

# Removendo em uma determinada posição
print("--Removendo em uma determinada posição--")
lista.pop(0)
for cor in lista:
    print(cor)

# Inserindo em uma determinada posição
print("--Inserindo em uma determinada posição--")
lista.insert(len(lista), "rosa")
for cor in lista:
    print(cor)

# Removendo especificamente uma cor
lista.remove("rosa")
print(lista)
