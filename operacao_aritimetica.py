def adicao(n1, n2, n3):
    try:
        if type(n1) is int or type(n1) is float and \
            type(n2) is int or type(n2) is float and \
            type(n3) is int or type(n3) is float:
            print(n1 + n2 + n3)
    except:
         print("Por Favor, informe apenas numero!")

quadrado = lambda n1: print(n1*n1)  # condição para usar quando apenas for escrito em 1 linha

# def quadrado(n1):
#     print(n1*n1)

def par(n1):
    print("par" if n1 %2 == 0 else "impar")

par = lambda n1: print("par" if n1 %2 == 0 else "impar")

def exponenciacao(n1, n2):
    i = 0
    while i < n2:
        repete = n1*n1
        i = i + 1
    print(repete)
