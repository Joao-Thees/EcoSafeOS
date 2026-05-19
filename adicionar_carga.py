from registro import centro_de_reciclagem

def adicionar_carga():
    id_centro = input('Digite o ID do centro de reciclagem: ')

    if id_centro not in centro_de_reciclagem:
        print(f'Centro "{id_centro}" não encontrado.')
        return

    novo_peso = float(input('Digite o peso da nova carga de resíduos (em kg): '))
    novos_creditos = int(novo_peso // 100)

    centro_de_reciclagem[id_centro]['residuos'].append(novo_peso)
    centro_de_reciclagem[id_centro]['saldo_creditos'] += novos_creditos

    centro = centro_de_reciclagem[id_centro]
    print(f'\nCarga adicionada ao centro {centro["nome"]}!')
    print(f'Novos créditos gerados: {novos_creditos} CO₂e')
    print(f'Saldo total de créditos: {centro["saldo_creditos"]} CO₂e')
