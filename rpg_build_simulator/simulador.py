from equipamento import Arma

def encontrar_melhor_build(personagem, bau):
    """
    Testa todas as armas disponíveis no baú e identifica
    qual gera o maior dano médio.
    """
    if len(bau) == 0:
        print("O baú está vazio! Não há armas para testar")
        return

    maior_dm = 0
    melhor_item = ""

    armar_original = personagem.arma_atual

    for arma in bau:

        if isinstance(arma, Arma):
            personagem.equipar_item(arma, rodar_autosave=False)
            personagem.calcular_status_finais()

            media_atual, total_atual = personagem.calcular_dano_medio()

            if media_atual > maior_dm:
                maior_dm = media_atual
                melhor_item = arma.nome_equipamento
    
    if armar_original is not None:
        personagem.equipar_item(armar_original, rodar_autosave=False)
    else:
        personagem.arma_atual = None

    personagem.calcular_status_finais()

    if melhor_item != "":
        print(f"\nA melhor arma é: {melhor_item} com dano médio de {maior_dm:,.2f}")
    else: 
        print("\nNenhuma arma foi encontrada dentro do baú!") 