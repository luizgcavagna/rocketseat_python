# @classmethod
# @staticmethod

class MinhaClasse:

    valor = 0 # Atributo de classe

    def __init__(self, nome):
        self.nome = nome
    
    # requer uma instancia para ser chamado
    def metodo_instancia(self):
        return f"Metodo de instancia chamado para {self.nome}"
    
    @classmethod
    def metodo_classe(cls):
        return f"Metodo de classe chamado para valor={cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Metodo estatico"
    
obj = MinhaClasse(nome="Class exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(obj.valor)
print(MinhaClasse.metodo_classe())
print(obj.metodo_classe())
print(MinhaClasse.metodo_estatico())
print(obj.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
configuracao1= "Fusca,volks,1970"
carro1 = Carro.criar_carro(configuracao=configuracao1)
print(f"\nMarca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}\n")

class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(a=1, b=-1))