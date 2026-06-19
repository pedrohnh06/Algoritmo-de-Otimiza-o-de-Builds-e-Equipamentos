from random import randint

class Equipamento:

    def __init__(self, nome_equipamento, bonus_ataque, bonus_dano_critico, raridade, chance_critico):
        self.nome_equipamento = nome_equipamento
        self.bonus_ataque = bonus_ataque
        self.bonus_dano_critico = bonus_dano_critico
        self.raridade = raridade
        self.chance_critico = chance_critico

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

        return self.equipamento_atual, self.inventario

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

    def calcular_dps_medio(self):
        dano_total = 0
        for i in range(1000):
            dano_total += self.simular_ataque()
        media_dano = dano_total/1000
        return media_dano, dano_total

p1 = Personagem("Galahad", 525, 750, 20)
e1 = Equipamento("Necro Espada", 10000, 13000, "Lendária", 99)

p1.equipar_item(e1)

p1.calcular_status_finais()
print(f"Ataque final do {p1.nome}: {p1.ataque_final}\nPorcentagem de Crítico:{p1.porcentagem_critica_final}%")

print(f"Testando a rotação de ataques")
print(p1.calcular_dps_medio())