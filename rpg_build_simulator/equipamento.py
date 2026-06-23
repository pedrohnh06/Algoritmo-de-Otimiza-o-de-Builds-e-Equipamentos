# Classe responsável por armazenar os atributos de um equipamento
class Equipamento:

    def __init__(self, nome_equipamento, bonus_ataque, bonus_dano_critico, raridade, chance_critico):
        self.nome_equipamento = nome_equipamento
        self.bonus_ataque = bonus_ataque
        self.bonus_dano_critico = bonus_dano_critico
        self.raridade = raridade
        self.chance_critico = chance_critico