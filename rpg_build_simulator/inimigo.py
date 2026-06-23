import time

class Inimigo:

    def __init__(self, nome, hp_maximo, defesa_percentual, ataque_base):
        self.nome = nome
        self.hp_maximo = hp_maximo
        self.hp_atual = hp_maximo
        self.defesa_percentual = defesa_percentual
        self.ataque_base = ataque_base

    def receber_dano(self, dano_bruto):
        dano_real = dano_bruto * (1 - (self.defesa_percentual / 100))
        self.hp_atual -= dano_real

        self.hp_atual = max(0, self.hp_atual)

        return dano_real

    def causar_dano(self, alvo):
        alvo.hp_atual -= self.ataque_base
        '''alvo.hp_atual -= max(0, alvo.hp_atual)'''
