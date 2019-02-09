flag = True
while flag:
    try:
        numero = int(input("Digite um numero"))
        if numero <= 0:
            print("Digite um numero positivo")
        else:
            flag = False
    except:
        flag = True

multiplicador = 0

while multiplicador <= 10:
    r = numero * multiplicador
    print("%d X %d = %d" % (numero, multiplicador, r))
    multiplicador += 1

