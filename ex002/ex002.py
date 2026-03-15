#AULA 02

# Declaração da classe
class Gafanhoto:
  """
  Essa classe cria um objeto do tipo Gafanhoto.
  Que tem os atributos nome e idade.
  """
  def __init__(self, nome = '', idade = 0):
    # Atributos de instâncias
    self.nome = nome
    self.idade = idade

  # Métodos instâncias
  def aniversario(self):
    self.idade += 1

  def __str__(self) -> str: # Dunder Method
    return f'{self.nome} é Gafanhota(a) e tem {self.idade} anos de idade'


# Declaração de objetos
g1 = Gafanhoto("Jorge mikael", 26)
g1.aniversario()
print(g1)
print(g1.__dict__) # Atributo
print(g1.__getstate__()) # Method
print(g1.__class__)
print(g1.__doc__) # Dunder Attribute