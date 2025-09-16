# POO
# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Ola, meu nome e {self.nome} e eu tenho {self.idade} anos."
    
# Objetos
pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(pessoa1.nome)
print(pessoa1.idade)
print(mensagem)

pessoa2 = Pessoa("Luiz", 30)
mensagem = pessoa2.saudacao()
print(mensagem)