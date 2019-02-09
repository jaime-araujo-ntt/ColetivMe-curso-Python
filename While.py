maior = 0
vezes = 0
while vezes < 10:
    num = int(input("digite um numero:"))
    if num > maior:
        maior = num
    vezes = vezes + 1
print(maior)
