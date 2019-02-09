"""letra = input('Digite uma letra')
letra = letra.upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'
        print("É vogal")
else:
    print("É consoante")"""

######### 2° VERSÃO ######### inserir tratamento de erro
vogais = ['A', 'E', 'I', 'O', 'U']

as = False
while l:
    try:
    letra = input("Digite uma letra:")
    letra = letra.upper()
    kkkk = False
    if letra in vogais:
    print("É Vogal!")
    else:
    print("É Consoante!")