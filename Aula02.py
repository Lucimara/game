class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Dog(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade) # pode invocar o método da classe pai de duas formas
        # Animal.__init__(self, nome, idade)

    familia = 'Canino'

    # def __init__(self, idade):
    #     self.idade = idade


# rex = Dog(4)
rex = Dog('Filomeno', 10)

# print(rex)
print(f'A idade do {rex.nome} é: {rex.idade}')
print(f'Ele pertence a familia: {rex.familia}')
print(f'É do tipo {rex.__class__.__name__}')
