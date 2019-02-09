import datetime        # interpretar e saber onde irá buscar

x = datetime.datetime.now()    # executa uma subfunção da função "datetime", dentro da biblioteca importada

nascimento = input('Informe a data de nascimento (dd/mm/aaaa):')

lista = nascimento.split('/')   # SPLIT é uma função que quebra textos com algo que se determina
print(lista)
lista = [int(i) for i in lista]  # transformando str em int separando pelo for e salvando numa lista

dias = ((x.year - lista[2])*360) + ((x.month - lista[1])*30) + ((x.day - lista[0]))

if dias <= 1:
    print(dias, "dia")
else:
    print(dias, "dias")
