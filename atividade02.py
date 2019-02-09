# Declarando váriaveis e guardando os numeros

n1 = 0
lista = []
while n1 < 4:
    nota = int(input("Inserir nota aqui: "))
    lista.append(nota)
    n1 += 1
print(len(lista))
print("sua média é %.1f" % ((lista[0]+lista[1]+lista[2]+lista[3])/len(lista)))
# soma = 0
# for i in lista:
#     print(i)
#     valor = lista[i]
#     soma = soma+valor
#     i += 1
# media = soma/len(lista)
# print("A média é: %d" % media)

"""n2 = float(input('Insira o segundo número:'))
n3 = float(input('Insira o terceiro número:'))
s = (n1 + n2 + n3)
# r = (n1 + n2 + n3) / 3
r = [n1, n2, n3]
""" 
"""
splitando = r.split(',')
print(r)
print("a media é: {:.1f}".format(s/len(r))) 
"""
""" print('A média dos 3 numeros é igual a: {}'.format(r))
# print('A média foi', r,', mas a soma deu', s)
# print('A média foi {}, mas a soma deu {}'.format(r, s))
#print('A média foi %f, mas a soma deu %f' %r , s)  //  ERRO!
print(type(r), type(s))"""


