                    # CÁLCULO DO VOLUME DO CILINDRO
""" comentando
em 
várias 
linhas
"""
import math
r = float(input("Insira o Raio do Cilindro em metros:"))
h = float(input("Insira a Altura do Cilindro em Metros:"))
# v = 3.14*pow(r, 2)*h
v = (math.pi*r**2)*h
print("O volume do Cilindro é: %.1f m³!" % v)
print("Com o raio %.1fm e altura %.1fm  o volume é: %.1fm³" % (r, h, v))
