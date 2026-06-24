from personagem import Personagem
from equipamento import Arma, Armadura
from simulador import encontrar_melhor_build
from inimigo import Inimigo
from arena import arena_batalha

#Criação do personagem
p1 = Personagem("Player 1", 525, 700, 10, 1000, 10)

e1 = Arma("Espada de Diamante", "Épica", 1500, 1900, 25)
e2 = Arma("Mjonir", "Mítica", 5500, 6500, 65)

armadura1 = Armadura("Armadura de Vibranium", "Mítica", 10, 5000)

bau_de_armas = [e1, e2]

#Equipa os itens criados
p1.equipar_item(e2)
p1.equipar_item(armadura1)

#Calcula os status finais do personagem
p1.calcular_status_finais()

#Cria o inimigo
i1 = Inimigo("Knull", 150000, 5, 100)

#Inicia a batalha
arena_batalha(p1, i1)

#encontrar a arma com melhor dano médio
'''encontrar_melhor_build(p1, bau_de_armas)'''
