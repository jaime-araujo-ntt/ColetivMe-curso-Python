altura = float(input("Insira sua altura:"))
sexo = input("Insira seu sexo:")
if sexo == 'masculino':                 # o comando IS só não funciona com string
    m = (72.7 * altura) - 58
    print('Seu peso ideal é %.2f Kg' % m)
elif: sexo == 'feminino':
    f = (62.1 * altura) - 44.7
    print('Seu peso ideal é %.2f Kg' % f)
else:
    print("voce deve ter digitado sexo errado")