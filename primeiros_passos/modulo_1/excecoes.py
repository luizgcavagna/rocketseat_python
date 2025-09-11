print("Exemplo de captura de execoes")

try:
    numero = int(input("Digite um numero inteiro: "))
    resultado = 10 / numero
    
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operacao finalizada")