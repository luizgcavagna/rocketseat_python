#exemplo de heranca
class Animal:
    def __init__(self, nome)-> None:
        self.nome = nome
    
    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro("Aria")
cat = Gato(nome="Thor")

dog.andar()
cat.andar()

animais = [dog, cat]

for animal in animais:
    print("O %s faz: %s" % (animal.nome, animal.emitir_som()))

print("\nExemplo de encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(1000)
print(f"Saldo: {conta.consultar_saldo()}")
conta.depositar(500)
print(f"Saldo: {conta.consultar_saldo()}")
conta.depositar(-500)
print(f"Saldo: {conta.consultar_saldo()}")
conta.sacar(200)
print(f"Saldo: {conta.consultar_saldo()}")

print("\nExemplo de abstracao:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return "Ligado usando a chave"
    
    def desligar(self):
        return "Desligado usando a chave"
    
fusca = Carro()
print(fusca.ligar())
print(fusca.desligar())