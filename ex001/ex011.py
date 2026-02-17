# Declaração de Class
class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return  f'{self.nome} é Gafanhot(a) e tem {self.idade} anos de idade.'

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 20
print(g1.mensagem())