from random import randint
from equipamento import Arma, Armadura
import json

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
        self.hp_maximo_final = hp_maximo


    def equipar_item(self, equipamento, rodar_autosave = True) -> None:
        #Equipa os itens criados
        if equipamento not in self.inventario:
            self.inventario.append(equipamento)

        if isinstance(equipamento, Arma):
            self.arma_atual = equipamento
            if rodar_autosave:
                print(f"🗡️ Arma [{equipamento.nome_equipamento}] equipada com sucesso!")

        elif isinstance(equipamento, Armadura):
            self.armadura_atual = equipamento
            if rodar_autosave:
                print(f"🛡️ Armadura [{equipamento.nome_equipamento}] vestida com sucesso!")
        else:
            print("⚠️ Tipo de equipamento desconhecido!")
        
        self.calcular_status_finais()

        if rodar_autosave:
            self.salvar_estado()

    def calcular_status_finais(self):
        # Reset para os valores base
        self.ataque_final = self.ataque_base
        self.porcentagem_critica_final = self.chance_critico
        self.dano_critico_final = self.dano_critico_base
        self.esquiva_final = self.esquiva
        self.hp_atual = self.hp_maximo
        self.hp_maximo_final = self.hp_maximo

        teto_antigo = self.hp_maximo_final

        #Calcula os status finais do personagem de acordo com os itens equipados
        if self.arma_atual is not None:
            self.ataque_final = self.ataque_base + self.arma_atual.bonus_ataque
            self.porcentagem_critica_final += self.arma_atual.chance_critico
            self.dano_critico_final += self.arma_atual.bonus_dano_critico

        if self.armadura_atual is not None:
            self.esquiva_final += self.armadura_atual.bonus_esquiva
            self.hp_maximo_final += self.armadura_atual.hp_adicional

        self.porcentagem_critica_final = min(self.porcentagem_critica_final, 75)

        if self.hp_maximo_final > teto_antigo:
            self.hp_atual += (self.hp_maximo_final - teto_antigo)

        if self.hp_atual > self.hp_maximo_final:
            self.hp_atual = self.hp_maximo_final

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

    def salvar_estado(self):
        salvar_estado = {"nome": self.nome,
        "hp_atual": self.hp_atual,
        "ataque_base": self.ataque_base,
        "chance_critico": self.chance_critico,
        "dano_critico_base": self.dano_critico_base,
        "esquiva": self.esquiva,
        "arma_atual": "",
        "armadura_atual": ""}

        if self.arma_atual is not None:
            salvar_estado["arma_atual"] = self.arma_atual.nome_equipamento

        if self.armadura_atual is not None:
            salvar_estado["armadura_atual"] = self.armadura_atual.nome_equipamento

        with open("save.json", "w") as arquivo:
            json.dump(salvar_estado, arquivo, indent=4)

    def carregar_estado(self, bau_de_armas):
        with open("save.json", "r") as arquivo:
            dados_carregados = json.load(arquivo)

        self.nome = dados_carregados["nome"]
        self.ataque_base = dados_carregados["ataque_base"]
        self.chance_critico = dados_carregados["chance_critico"]
        self.dano_critico_base = dados_carregados["dano_critico_base"]
        self.esquiva = dados_carregados["esquiva"]

        self.inventario = []

        for item in bau_de_armas:
            if item.nome_equipamento == dados_carregados.get("arma_atual"):
                self.equipar_item(item)
            elif item.nome_equipamento == dados_carregados.get("armadura_atual"):
                self.equipar_item(item)


        self.calcular_status_finais()
        self.hp_atual = dados_carregados["hp_atual"]
