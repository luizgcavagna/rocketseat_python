print("Exemplo de importacao de um modulo padrao:")
from math import sqrt
# import Math

numero = int(input("Escolha o numero para verificar a raiz quadrada: "))
raiz_quadrada = sqrt(numero)

print(f"A raiz quadrada de {numero} e {raiz_quadrada}")

print("\nExemplo de criacao de modulo")
import meu_modulo
# from meu_modulo import saudacao, dobro

mensagem = meu_modulo.saudacao("Luiz")
dobro = meu_modulo.dobro(numero)

print(mensagem)
print(f"O dobro de {numero} e {dobro}")