from registro import centro_de_reciclagem
def cadastrar_centro():
    
    id_centro = input('Digite o ID do seu centro de reciclagem. ex: "C01": ')
    nome_unidade = input('Digite o nome da sua unidade: ')
    pesos_residuos_processados = float(input('Digite o peso total dos resíduos processados (Em KG): '))
    credito_de_carbono = 0

    for _ in range(int(pesos_residuos_processados // 100)): # range com conversao de dado float para inteiro pois o for nao trabalha com dados float.
        if pesos_residuos_processados >= 100.00:
            credito_de_carbono += 1
            

    centro_de_reciclagem[id_centro] = {"nome": nome_unidade,
                                       "residuos": [pesos_residuos_processados],
                                       "saldo_creditos": credito_de_carbono} #adicionando id ao dicionario
    
    

cadastrar_centro()
print(centro_de_reciclagem)
