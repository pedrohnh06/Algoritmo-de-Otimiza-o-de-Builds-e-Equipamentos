# Classe responsável por armazenar os atributos de um equipamento
class Equipamento:

    def __init__(self, nome_equipamento, raridade):
        self.nome_equipamento = nome_equipamento
        self.raridade = raridade

class Arma(Equipamento):
    def __init__(self, nome_equipamento, raridade ,bonus_ataque, bonus_dano_critico, chance_critico): 
        super().__init__(nome_equipamento, raridade)

        self.bonus_ataque = bonus_ataque
        self.bonus_dano_critico = bonus_dano_critico
        self.chance_critico = chance_critico

class Armadura(Equipamento):
    def __init__(self, nome_equipamento, raridade, bonus_esquiva, hp_adicional=0):
        super().__init__(nome_equipamento, raridade)

        self.bonus_esquiva = bonus_esquiva
        self.hp_adicional = hp_adicional
