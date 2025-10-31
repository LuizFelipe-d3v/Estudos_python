class Animal:
    def __init__(self, nome, comida):
        self.nome = nome
        self.comida = comida

    def comer(self):
        return f'{self.nome} esta comendo uma {self.comida}'
      
    def satisfeito(self):
        if self.comida == 'hiena':
            return 'Leao esta satisfeito'
        else:
            return 'Leao ainda tem fome'

leao = Animal('Leao', 'girafa')

print(leao.nome)
print(leao.comer())
print(leao.satisfeito())
