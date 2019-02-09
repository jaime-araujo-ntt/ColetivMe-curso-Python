############ CRIANDO OBEJETO PARA USARIOS ##############
lista_objetos = [
{"nome": "Jaime Neto", "usuário": "jaime.nt", "senha": "Eu2019"},
{"nome": "janiffer do Tinder", "usuário": "Jenni", "senha": "Tinder2019"}
]
estado = True
while estado:
    usuario = input("Informe o nome do usuário: ")
    senha = input("Informe a senha: ")
    achei_usuario = False
    achei_senha = False

    for objeto in lista_objetos:
        if usuario == objeto["usuário"] and senha == objeto["senha"]:
            achei_usuario = True
            ache_senha = True
    if achei_usuario and ache_senha:
        print("Acesso permitido!")
        estado = False
    else:
        print("Usuário ou Senha errada!")

"""
print("-"*20, "imprimindo com while", "-"*20)
i = 0
while i < len(lista_objetos):
    print(lista_objetos[i]["usuário"])
    i += 1

print("-"*20, "imprimindo com for", "-"*20)
for objeto in lista_objetos:
    print(objeto["nome"])

print("-"*20, "imprimindo lista com for", "-"*20)
for o in lista_objetos:
    # print("O usuário:", o["usuário"], "e a senha:", o["senha"])
    print("O usuário: {} e a sneha: {}".format(o["usuário"], o["senha"]))"""
# senha_cad = "Eu2019"
# usuario = input("informe o nome do usuário:")
# senha = input("informe a senha:")
# print("Cadastrado")
# while senha != senha_cad:
#     print("senha errada!")
#     senha = input("Informe a senha:")