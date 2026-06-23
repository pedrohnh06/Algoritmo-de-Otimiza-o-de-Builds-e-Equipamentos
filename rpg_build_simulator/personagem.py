from random import randint

# Classe principal do sistema de combate.
# Um personagem possui atributos base, inventário e equipamento equipado.
class Personagem:

    def __init__(self, nome, ataque_base, dano_critico_base, chance_critico, hp_maximo):
        self.nome = nome
        self.ataque_base = ataque_base
        self.dano_critico_base = dano_critico_base
        self.chance_critico = chance_critico
        self.equipamento_atual = None
        self.inventario = []
        self.ataque_final = ataque_base
        self.porcentagem_critica_final = chance_critico
        self.dano_critico_final = dano_critico_base 
        self.hp_maximo = hp_maximo
        self.hp_atual = hp_maximo


    def equipar_item(self, equipamento) -> None:
        self.inventario.append(equipamento)
        self.equipamento_atual = equipamento

    def calcular_status_finais(self):
        if self.equipamento_atual is not None:
            self.ataque_final = self.ataque_base + self.equipamento_atual.bonus_ataque
            self.porcentagem_critica_final += self.equipamento_atual.chance_critico
            self.dano_critico_final += self.equipamento_atual.bonus_dano_critico

        self.porcentagem_critica_final = min(self.porcentagem_critica_final, 75)

    def simular_ataque(self):
        """
        Simula um único ataque considerando
        chance de crítico e dano crítico.
        """

        chance = randint(1, 100)
        golpe_normal = self.ataque_final
        golpe_critico = self.ataque_final

        if chance <= self.porcentagem_critica_final:
            golpe_critico = self.ataque_final + self.dano_critico_final
            return golpe_critico
        else:
            return golpe_normal

    def calcular_dano_medio(self) -> tuple:
        """
        Simula 1000 ataques para estimar o dano médio causado
        pelo personagem com o equipamento atualmente equipado.
        """
        dano_total = 0
        numero_simulacoes = 1000

        for i in range(numero_simulacoes):
            dano_total += self.simular_ataque()
        media_dano = dano_total/numero_simulacoes

        return media_dano, dano_total