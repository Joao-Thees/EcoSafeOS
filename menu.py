from cadastro import cadastrar_centro
from adicionar_carga import adicionar_carga

def menu():
    print('''
                    
                   ___           _
             ___  / __\ ___  ___| |__   ___
            / _ \/ /   / _ \/ __| '_ \ / _ \
            |  __/ /___| (_) \__ \ | | | (_)|
            \___\____/ \___/|___/_| |_|\___/

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

  🌿  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  🌿
      Protecting the digital ecosystem
      v1.0.0  |  Secure. Green. Aware.
  🌱  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  🌱

    ~   ~   ~   ~   ~   ~   ~   ~   ~
  🌳  EchoSafeOS  |  est. 2026  🌳
    ~   ~   ~   ~   ~   ~   ~   ~   ~
          
        Bem vindo ao EchoSafeOS, Uma startup focada em sustentabilidade está desenvolvendo o EcoSafe OS, um sistema
        via terminal para gerenciar centros de reciclagem. O objetivo da plataforma é registrar a
        quantidade de resíduos sólidos processados por cada centro e calcular automaticamente
        os créditos de carbono gerados por essa atividade. Vocês foram encarregados de
        desenvolver o núcleo (engine) deste sistema utilizando Python!
        
        By: Joao-Thees & Caiovfaria
          ''')
    
    print('''Escolha sua opção: 
          
        • 1 - Cadastrar Centro de Reciclagem
        • 2 - Registrar Processamento de Resíduos
        • 3 - Gerar Relatório Ambiental
        • 4 - Adicionar Carga a Centro Existente
        • 0 - Sair do Sistema ''')
    
    opcao = int(input('Digite aqui sua opção: '))

    match opcao:
        
        case 1:
            cadastrar_centro()

        case 4:
            adicionar_carga()


menu()
