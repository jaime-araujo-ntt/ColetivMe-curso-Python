                # CONVERSÃO DE TEMPERATURA

tc = float(input("Insira a temperatura atual em °C:"))
# tf = tc*1.8+32
tf = ((tc*9)/5)+32
print("%.1f°C equivale a %.1f°F" % (tc, tf))
