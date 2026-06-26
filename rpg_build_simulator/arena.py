import time
# Função principal do sistema de combate.
def arena_batalha(heroi, chefe):

    print(f"\n{'='*45}")
    print(f"⚔️  A BATALHA COMEÇOU: {heroi.nome} VS {chefe.nome} ⚔️")
    print(f"{'='*45}\n")

    turno = 1
    while heroi.hp_atual > 0 and chefe.hp_atual > 0:
        print(f"--- TURNO {turno} ---")
        time.sleep(0.5)

        #Turno do heroi
        ataque = heroi.simular_ataque()
        dano_causado = chefe.receber_dano(ataque)

        print(f"🗡️ {heroi.nome} desferiu um golpe! causando {dano_causado:.0f}, {chefe.nome} ficou com {chefe.hp_atual:.0f} de HP.")
        
        if chefe.hp_atual <= 0:
            print(f"\n👑 VITÓRIA! {chefe.nome} foi esmagado no turno {turno}!")
            heroi.salvar_estado()
            break
        
        time.sleep(1)

        #Turno do chefe
        chefe.causar_dano(heroi)
        print(f"💥 {chefe.nome} revidou com fúria! {heroi.nome} ficou com {heroi.hp_atual:.0f} de HP.\n")

        if heroi.hp_atual <= 0: 
            print(f"\n💀 DERROTA! {heroi.nome} não resistiu e caiu em combate...")
            heroi.inventario = []
            heroi.arma_atual = None
            heroi.armadura_atual = None
            heroi.calcular_status_finais()

            heroi.salvar_estado()
            break

        turno +=  1
        time.sleep(1.5)
