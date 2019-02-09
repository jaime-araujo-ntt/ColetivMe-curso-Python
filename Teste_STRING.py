frase = "To programando em Python"
print(frase[5]) # busca a string na posição escolhida
print(frase.startswith("To")) #saber se começa com a string escolhida
print(frase.lower())
print(frase.upper())
print("\"Oi\""), print("'Oi'"), print('"Oi"') # inserindo aspas na string
print("Python" in frase)
print("PHP" not in frase)
print(frase.count("Python")) # conta a ocorrencia da string
print(frase.find("Python")) # posição que inicia a string
print(frase.split(" ")) # secciona a string com o que for escolhido, transformando em lista
print(frase.strip()) # retira espaços antes e depois da string
print("{2} {1}, {0}!".format("BOA", "NOITE", "PESSOAL"))  # o FORMART chama na ordem selecionada

