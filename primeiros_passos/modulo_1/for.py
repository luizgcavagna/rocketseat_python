lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for elemento in lista:
    print(elemento)
    
print("\n")

tupla = ('a', 'b', 'c')

for elemento in tupla:
    print(elemento)

print("\n")

pessoa = {"nome": 0, "idade": 1, "cidade": 2, "estado": 3}

print("\nFor utilizando dicionario - chaves")
for elemento in pessoa.keys():
    print(elemento)

print("\nFor utilizando dicionario - valores")
for elemento in pessoa.values():
    print(elemento)

print("\n")

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print("\n")

# range(): intervalo numerico
# [0,1,2,3,4,5,6,7,8,9]
print(list(range(0, 10)))

print("\n")

for numero in range(5):
    print("Numero:", numero)

print("\n")

# Utilizando range() com len()
for indice in range(0, len(lista)):
    print("Indice:", indice)
    print("Elemento:", lista[indice])

print("\n")

# enumerate()
lista_enumerate = ["omega", "phi", "alpha"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")