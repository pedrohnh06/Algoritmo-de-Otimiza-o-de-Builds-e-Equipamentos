from random import randint

# Classe responsável por armazenar os atributos de um equipamento
class Equipamento:

    def __init__(self, nome_equipamento, bonus_ataque, bonus_dano_critico, raridade, chance_critico):
        self.nome_equipamento = nome_equipamento
        self.bonus_ataque = bonus_ataque
        self.bonus_dano_critico = bonus_dano_critico
        self.raridade = raridade
        self.chance_critico = chance_critico

# Classe principal do sistema de combate.
# Um personagem possui atributos base, inventário e equipamento equipado.
class Personagem:

    def __init__(self, nome, ataque_base, dano_critico_base, chance_critico):
        self.nome = nome
        self.ataque_base = ataque_base
        self.dano_critico_base = dano_critico_base
        self.chance_critico = chance_critico
        self.equipamento_atual = None
        self.inventario = []

    def equipar_item(self, equipamento):
        self.inventario.append(equipamento)
        self.equipamento_atual = equipamento

    def calcular_status_finais(self):
        self.ataque_final = self.ataque_base
        self.porcentagem_critica_final = self.chance_critico
        self.dano_critico_final = self.dano_critico_base 
        
        if self.equipamento_atual != None:
            self.ataque_final = self.ataque_base + self.equipamento_atual.bonus_ataque
            self.porcentagem_critica_final += self.equipamento_atual.chance_critico
            self.dano_critico_final += self.equipamento_atual.bonus_dano_critico

        self.porcentagem_critica_final = min(self.porcentagem_critica_final, 75)

    def simular_ataque(self):
        chance = randint(1, 100)
        golpe_normal = self.ataque_final
        golpe_critico = self.ataque_final

        if chance <= self.porcentagem_critica_final:
            golpe_critico = self.ataque_final + self.dano_critico_final
            return golpe_critico
        else:
            return golpe_normal

    def calcular_dano_medio(self):
        """
        Simula 1000 ataques para estimar o dano médio causado
        pelo personagem com o equipamento atualmente equipado.
        """
        dano_total = 0

        for i in range(1000):
            dano_total += self.simular_ataque()
        media_dano = dano_total/1000

        return media_dano, dano_total

p1 = Personagem("Player 1", 525, 700, 10)
e1 = Equipamento("Espada de Diamante", 1500, 1900, "Épica", 25)
e2 = Equipamento("Espada Básica", 250, 400, "Comum", 18)
e3 = Equipamento("Mjonir", 5500, 6500, "Mítica", 45)
bau_de_armas = [e1, e2, e3]

def encontrar_melhor_build():
    """
    Testa todas as armas disponíveis no baú e identifica
    qual gera o maior dano médio.
    """
    if len(bau_de_armas) == 0:
        print("O baú está vazio! Não há armas para testar")
        return

    maior_dps = 0
    melhor_item = ""

    for arma in bau_de_armas:
        p1.equipar_item(arma)
        p1.calcular_status_finais()

        media_atual, total_atual = p1.calcular_dano_medio()

        if media_atual > maior_dps:
            maior_dps = media_atual
            melhor_item = arma.nome_equipamento

    print(f"\nA melhor arma é: {melhor_item} com DPS médio de {maior_dps:.2f}")

#Código Principal:
encontrar_melhor_build()