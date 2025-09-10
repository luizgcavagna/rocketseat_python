#tupla de exemplo
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 0)

print("tupla:", tupla)

print("tupla[0]", tupla[0])
print("tupla[3]", tupla[3])
print("tupla[-1]", tupla[-1])

#metodo count
contagem = tupla.count(0)
print("Quantidade de vezes que elemento 0 aparece: ", contagem)

indice = tupla.index(0)
print("Indice: ", indice)