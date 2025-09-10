# if, elif e else

#exemplo de "if"
idade = int(input("Quantos anos voce tem? "))


if idade >= 18:
    print("Maior de idade")

if idade == 19:
    print("Voce tem 19 anos")

if idade < 18:
    print("Menor de idade")

if idade != 10:
    print("Voce nao tem 10 anos")

# exemplo "if" & "else"
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de Idade")

# exemplo "if", "elif" & "else"
if idade >= 18:
    print("Maior de idade")
if idade >= 12 and idade <= 18:
    print("Voce e um adolescente")
else:
    print("Voce e uma crianca")

mensagem = "Pode tirar a carteira de habilitacao" if idade >= 18 else "Aguarde"
print(mensagem)