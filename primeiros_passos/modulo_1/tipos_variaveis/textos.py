# Declaracao
nome_completo = "Luiz Gustavo" + ' Cavagna'

aspas = """ 
    Hello
    World
"""

nome_completo_quebra = "Luiz \
Gustavo"

nome = "Luiz"
sobrenome = "Cavagna"

print(aspas)
print(nome_completo_quebra)

# Formatacao
print("Nome (1a forma):", nome_completo)
print("Nome (2a forma):" + nome_completo)
print("Nome (3a forma):" + "Luiz" + "Gustavo")
print("Nome (4a forma):" + "Luiz", "Gustavo")
print("Nome (5a forma): %s" % nome_completo)
print("Nome (6a forma): %s %s" % (nome, sobrenome))
print(f"Nome (7a forma): {nome} {sobrenome}")
print("Nome (8a forma): {} {}".format(nome, sobrenome))

print(nome.upper())
print(nome.lower())
print(nome[0])

print(nome_completo.count("a"))
print(nome.encode())
print(nome_completo.replace("a", "7"))

telefone = "(16) 98110-7195"
print(telefone.replace("(", "").replace(")", "").replace("-", ""))

print("-".join(nome))
print(nome_completo.split(" "))

# remove do comeco e do fim
nome_x = "xLuiz Gustavox"
print(nome_x.strip("x"))
# so a direita 
print(nome_x.rstrip("x"))
# so a esquerda 
print(nome_x.lstrip("x"))

print(nome_completo.startswith("Lu"))

print("avo" in nome_completo)
print("abc" not in nome_completo)