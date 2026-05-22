from registro import centro_de_reciclagem

def relatorio_formatado():
    for chave, valor in centro_de_reciclagem.items():
        print(f'\n ID CENTRO: {chave}\n NOME_CENTRO: {valor["nome"]}\n CRÉDITOS DE CARBONO: {valor["saldo_creditos"]} CO₂e\n')
        print(f'Essa atividade gerou {valor["saldo_creditos"]} CO₂e! ')

        return centro_de_reciclagem
    # exibindo cada chave e valor de forma formatada.
    # valor recebe chaves