from personagem import Personagem
from equipamento import Equipamento
from simulador import encontrar_melhor_build
from inimigo import Inimigo
from arena import arena_batalha

p1 = Personagem("Player 1", 525, 700, 10, 1000)

e1 = Equipamento("Espada de Diamante", 1500, 1900, "Épica", 25)
e2 = Equipamento("Espada Básica", 250, 400, "Comum", 18)
e3 = Equipamento("Mjonir", 5500, 6500, "Mítica", 65)
bau_de_armas = [e1, e2, e3]

p1.equipar_item(e2)
p1.calcular_status_finais()


i1 = Inimigo("Knull", 150000, 5, 250)

arena_batalha(p1, i1)

#encontrar a arma com melhor dano médio
'''encontrar_melhor_build(p1, bau_de_armas)'''
