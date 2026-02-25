class Animal:
    def __init__(self, nome, idade = int):
        self.nome = nome
        self.idade = idade

    def emitir_som():
        return print("O animal emitiu um som genérico")

class Gato(Animal):
    def emitir_som(self):
        return print(f"o {self.nome} miou !")

class Cachorro(Animal):
    def emitir_som(self):
        return print(f"O {self.nome} latiu !")

gato = Gato("Ceni", 5)
cachorro = Cachorro("Douglas", 10)

gato.emitir_som()
cachorro.emitir_som()
        
