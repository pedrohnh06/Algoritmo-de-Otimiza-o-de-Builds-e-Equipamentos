from personagem import Personagem
from equipamento import Arma, Armadura
from simulador import encontrar_melhor_build
from inimigo import Inimigo
from arena import arena_batalha

def inicializar_banco_de_dados():
    e1 = Arma("Espada de Diamante", "Épica", 1500, 1900, 25)
    e2 = Arma("Mjonir", "Mítica", 5500, 6500, 65)
    armadura1 = Armadura("Armadura de Vibranium", "Mítica", 10, 15000)
    bau_de_armas = [e1, e2, armadura1]

    i1 = Inimigo("Knull", 50000, 5, 350)

    return bau_de_armas, i1

def main():
    print("Inicializando RPG Build Simulator...")

    bau_de_armas, knull = inicializar_banco_de_dados()

    p1 = Personagem("Player 1", 525, 700, 10, 1000, 10)

    try:
        p1.carregar_estado(bau_de_armas)
        print("💾 Save carregado com sucesso!")
    except FileNotFoundError:
        print("📝 Novo jogo iniciado! Nenhum save anterior encontrado.")
        # Já força o salvamento de um arquivo zerado para o jogador não ter problemas depois
        p1.salvar_estado()

    while True:
        print("\n" + "="*42)
        print(" O QUE VOCÊ DESEJA FAZER?")
        print(" 1 - Ir para Arena de Batalha")
        print(" 2 - Rodar Simulador de Dano Médio(Builds)")
        print(" 3 - Abrir Baú / Equipar Itens")
        print(" 4 - Descansar (Recuperar 100% do HP)")
        print(" 5 - Sair do Jogo")
        print("="*42)

        escolha = input("Digite o número da ação: ").strip()

        if escolha == "1":
            arena_batalha(p1, knull)
            if p1.hp_atual <= 0 or knull.hp_atual <= 0:
                _, knull = inicializar_banco_de_dados()
        
        elif escolha == "2":
            encontrar_melhor_build(p1, bau_de_armas)

        elif escolha == "3":
            print("\n" + "-"*30)
            print("🎒 BAÚ DE EQUIPAMENTOS:")

            for indice, item in enumerate(bau_de_armas):
                tipo = "Arma" if isinstance(item, Arma) else "Armadura"
                print(f" [{indice}] - {tipo}: {item.nome_equipamento} ({item.raridade})")
                print("-"*30)
            
            escolha_item = input("Digite o número do item para equipar (ou 'V' para voltar): ").strip().upper()
            if escolha_item == 'V':
                continue

            elif escolha_item.isdigit() and 0 <= int(escolha_item) < len(bau_de_armas):
                item_selecionado = bau_de_armas[int(escolha_item)]
                
                p1.equipar_item(item_selecionado)
            else:
                print("❌ Opção inválida no baú!")

        elif escolha == "4":
            if p1.hp_atual < p1.hp_maximo_final:
                p1.hp_atual = p1.hp_maximo_final
                p1.salvar_estado()
                print("💤 Você descansou na estalagem. HP restaurado ao máximo!")
            else:
                print("✨ Sua vida já está cheia! Não é preciso descansar.")

        elif escolha == "5":
            print("Saindo do jogo... Até a próxima!")
            break

        else:
            print("❌ Comando inválido. Tente Novamente.")

if __name__ == '__main__':
    main()