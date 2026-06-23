def encontrar_melhor_build(personagem, bau):
    """
    Testa todas as armas disponíveis no baú e identifica
    qual gera o maior dano médio.
    """
    if len(bau) == 0:
        print("O baú está vazio! Não há armas para testar")

    else: 
        maior_dps = 0
        melhor_item = ""

        for arma in bau:
            personagem.equipar_item(arma)
            personagem.calcular_status_finais()

            media_atual, total_atual = personagem.calcular_dano_medio()

            if media_atual > maior_dps:
                maior_dps = media_atual
                melhor_item = arma.nome_equipamento

        print(f"\nA melhor arma é: {melhor_item} com dano médio de {maior_dps:,.2f}")