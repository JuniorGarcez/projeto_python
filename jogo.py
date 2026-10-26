from heroi import Heroi
from inimigo import Inimigo

class Jogo:
  def __init__(self):
    self.heroi = Heroi(nome = "Heroi", vida=100, nivel= 5, habilidade="Super Força")
    self.inimigo = Inimigo(nome= "Morcego", vida=100, nivel=3, tipo="Voador")

  def iniciar_batalha(self):
    print("Iniciando Batalha")    
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      print("\nDetalhes dos Personagens: ")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("Pressione Enter para atacar")
      escolha = input("Escolha (1 - ataque normal, 2 - ataque especial)")

      if escolha == '1':
        self.heroi.atacar(self.inimigo)
      elif escolha == '2':
        self.heroi.ataque_especial(self.inimigo)
      else:
        print("Escolha inválida")

      if self.inimigo.get_vida() > 0:
        self.inimigo.atacar(self.heroi)

    print("\nGAME OVER")
    if self.heroi.get_vida() > 0:
      print("Parabéns, você venceu a batalha")
    else:
      print("Você Perdeu")
