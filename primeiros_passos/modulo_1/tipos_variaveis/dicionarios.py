# Criando um dicionario de exemplo
pessoa = {"nome": "Luiz", "idade": 30, "cidade": "Ribeirao preto"}

#exibindo
print("Dicionario: ",  pessoa)

#acessando por chave
print("Nome:", pessoa['nome'])
print("Idade:", pessoa['idade'])
print("Cidade:", pessoa['cidade'])

pessoa["sobrenome"] = "Cavagna"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

#remove um par chave-valor
del pessoa["sobrenome"]
print(pessoa)

#metodos: keys(), values(), items()
chaves = pessoa.keys()
print(chaves)
chaves_lista = list(chaves)#usa o list para transformar numa lista
print("Keys:", chaves_lista)
print("Primeira chave:", chaves_lista[0])

#metodos values
valores = pessoa.values()
print(valores)
valores_lista = list(valores)
print("Valores:", valores_lista)
print("Primeiro valor:", valores_lista[0])

#metodos items
itens = pessoa.items()
print(itens)
itens_lista = list(itens)
print("Pares chave-valor do dicionario", itens_lista)
print("Primeira chave valor: %s = %s" % (itens_lista[0][0], itens_lista[0][1]))