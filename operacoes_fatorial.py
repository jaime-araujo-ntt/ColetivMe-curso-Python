
def main():
    fatorial_whyle(5)
    fatorial_for(5)
    fatorial_recursivo(5)

def fatorial_whyle(n):
    n = int(input("Informe um numero: "))
    fat = 1

    while n >= 1:
        fat = n * fat    # sempre que eu quiser amrmazenar uma variável, ela tem que fazer parte para se renovar.
        n = n -1
    print(fat)

############## usando for ######################
def fatorial_for(numero):
    numero = int(input("Informe outro numero"))
    resultado = 1

    for i in range(numero):
        resultado = numero * resultado
        numero = numero - 1
    print(resultado)

################ Recursividade ########
###É fazer com que a função chame a ###
###própria função #####################

def fatorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return
    else:
        return numero * fatorial(numero - 1)

if __name__ == '__main__':
    main()