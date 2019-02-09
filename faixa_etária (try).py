numero = True
while numero:
    try:                                # tentar executar o que esta dentro.
        idade = int(input("digite sua idade:"))
        numero = False
    except:                             # se não conseguir entra no except.
        print("Por favor execute um valor numerico")
# finally:                              # mais uma chance para digitar certo. e entra com a pergunta novamente
#    idade = int(input("digite sua idade:"))

if 0 <= idade < 9:
    print("Mirim")
elif 9 <= idade < 14:
    print("Infantil")
elif 14 <= idade < 18:
    print("Juvenil")
elif idade >= 18:
    print("Adulto")
else:
    print("Viajante do Tempo!")
