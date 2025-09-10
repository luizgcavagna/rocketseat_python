# Exemplo
def saudacao(nome):
    print(f"Hello World, {nome}\n")

print("Chamando a funcao saudacao:\n")
saudacao("Luiz")

#Funcao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("Chamando funcao quadrado:\n")
resultado_quadrado = quadrado(9)
print("Resultado da funcao quadrado:", resultado_quadrado)
print(f"Resultado da funcao quadrado: {quadrado(2)} \n" )

# Funcao com multiplos parametros
def soma(n1, n2):
    return n1 + n2

print("Chamando funcao soma:\n")
print(f"Resultado da funcao soma: {soma(2, 2)} \n" )