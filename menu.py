from cadastro import cadastrar_centro
from adicionar_carga import adicionar_carga
from relatorio import relatorio_formatado
# inicie o programa pelo menu.
def menu():
    print('''

            ██████╗  █████╗ ███████╗███████╗
            ██╔════╝ ██╔══██╗██╔════╝██╔════╝
            ╚█████╗  ███████║█████╗  █████╗
            ╚═══██╗ ██╔══██║██╔══╝  ██╔══╝
            ██████╔╝ ██║  ██║██║     ███████╗
            ╚═════╝  ╚═╝  ╚═╝╚═╝     ╚══════╝

                ██████╗ ███████╗
                ██╔═══██╗██╔════╝
                ██║   ██║███████╗
                ██║   ██║╚════██║
                ╚██████╔╝███████║
                ╚═════╝ ╚══════╝
                ~   ~   ~   ~   ~   ~   ~   ~   ~
            🌳  EchoSafeOS  |  est. 2026  🌳
                ~   ~   ~   ~   ~   ~   ~   ~   ~
          
        Bem vindo ao EchoSafeOS, Uma startup focada em sustentabilidade está desenvolvendo o EcoSafe OS, um sistema
        via terminal para gerenciar centros de reciclagem. O objetivo da plataforma é registrar a
        quantidade de resíduos sólidos processados por cada centro e calcular automaticamente
        os créditos de carbono gerados por essa atividade. Vocês foram encarregados de
        desenvolver o núcleo (engine) deste sistema utilizando Python!
        
        By: Joao-Thees & Caiovfaria
          \n''')
    
    while True:
        print('''\nEscolha sua opção:

        • 1 - Cadastrar Centro de Reciclagem
        • 2 - Registrar Processamento de Resíduos
        • 3 - Gerar Relatório Ambiental
        • 4 - Adicionar Carga a Centro Existente
        • 0 - Sair do Sistema ''')

        opcao = int(input('\nDigite aqui sua opção: '))

        match opcao:

            case 1:
                cadastrar_centro()
            case 3:
                relatorio_formatado()
            case 4:
                adicionar_carga()
            case 0:
                print('Saindo do sistema...')
                break

if __name__ == "__main__":
    menu() # pro python reconhecer
