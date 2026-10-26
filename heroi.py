import random

from personagem import Personagem

class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade

  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\n Habilidade: {self.get_habilidade()}"

  def ataque_especial(self, alvo):
    dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} usou a habilidade especial em {alvo.get_nome()} e caudou {dano} de dano!")
