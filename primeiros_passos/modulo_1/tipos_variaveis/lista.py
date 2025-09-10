# Declaracao

lista = [0, 1, 2, 3, 4, 5, 6, "zero", True, False]

# exibindo lista
print("lista", lista)

# exibindo elementos da lista
print("lista[0]", lista[0])
print("lista[5]", lista[5])
print("lista[0:7]", lista[0:7])
print("lista[:7]", lista[:7])
print("lista[7:]", lista[7:])

# metodos de lista

#metodo append(): adiciona um elementoao final da lista
lista.append('bipolar')
print("Apos append():", lista)

#metodo index
indice =lista.index("zero")
print("Indice do elemento zero:", indice)

#metodo insert(): insere um elemento em um idice especifico
lista.insert(10, '+-')
print("Apos insert:", lista)

#metodo pop(): deleta da lista
elemento_removido = lista.pop(7)
print("Elemento removido", elemento_removido)
print("Apos pop(7):", lista)
print(type(lista))

#metodo remove()
lista.remove(False)
print("Apos remove(False):", lista)

#metodo sort()
lista_numerica = [1, 3, 0, 2, 4, 7, 5, 6]
lista_numerica.sort()
print("Apos sort(): ", lista_numerica)