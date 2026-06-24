from random import randint
from equipamento import Arma, Armadura

class Personagem:

    def __init__(self, nome, ataque_base, dano_critico_base, chance_critico, hp_maximo, esquiva):
        self.nome = nome
        self.ataque_base = ataque_base
        self.dano_critico_base = dano_critico_base
        self.chance_critico = chance_critico
        self.arma_atual = None
        self.armadura_atual = None
        self.inventario = []
        self.ataque_final = ataque_base
        self.porcentagem_critica_final = chance_critico
        self.dano_critico_final = dano_critico_base 
        self.hp_maximo = hp_maximo
        self.hp_atual = hp_maximo
        self.esquiva = esquiva
        self.esquiva_final = esquiva


    def equipar_item(self, equipamento) -> None:
        #Equipa os itens criados
        self.inventario.append(equipamento)

        if isinstance(equipamento, Arma):
            self.arma_atual = equipamento
            print(f"🗡️ Arma [{equipamento.nome_equipamento}] equipada com sucesso!")
        elif isinstance(equipamento, Armadura):
            self.armadura_atual = equipamento
            print(f"🛡️ Armadura [{equipamento.nome_equipamento}] vestida com sucesso!")
        else:
            print("⚠️ Tipo de equipamento desconhecido!")

    def calcular_status_finais(self):
        # Reset para os valores base
        self.ataque_final = self.ataque_base
        self.porcentagem_critica_final = self.chance_critico
        self.dano_critico_final = self.dano_critico_base
        self.esquiva_final = self.esquiva
        self.hp_atual = self.hp_maximo

        #Calcula os status finais do personagem de acordo com os itens equipados
        if self.arma_atual is not None:
            self.ataque_final = self.ataque_base + self.arma_atual.bonus_ataque
            self.porcentagem_critica_final += self.arma_atual.chance_critico
            self.dano_critico_final += self.arma_atual.bonus_dano_critico


        if self.armadura_atual is not None:
            self.esquiva_final += self.armadura_atual.bonus_esquiva
            self.hp_atual += self.armadura_atual.hp_adicional

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
