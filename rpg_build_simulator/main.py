from personagem import Personagem
from equipamento import Equipamento
from simulador import encontrar_melhor_build

p1 = Personagem("Player 1", 525, 700, 10)
e1 = Equipamento("Espada de Diamante", 1500, 1900, "Épica", 25)
e2 = Equipamento("Espada Básica", 250, 400, "Comum", 18)
e3 = Equipamento("Mjonir", 5500, 6500, "Mítica", 45)

bau_de_armas = [e1, e2, e3]

#Código Principal:
encontrar_melhor_build(p1, bau_de_armas)