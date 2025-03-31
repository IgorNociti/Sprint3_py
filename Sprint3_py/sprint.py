pedidos_mamadeiras = []
pedidos_remedios = []

""" Solicitação inicial de informações do usuário"""
quarto = input("Digite o número do quarto: ")
nome_usuario = input("Digite seu nome: ")
print(f"Bem-vindo(a), {nome_usuario}! Você está no quarto {quarto}.\n")

def solicitar_mamadeira():
    """Solicita uma mamadeira para um bebê."""
    nome_bebe = input("Digite o nome do bebê: ")
    quantidade = input("Digite a quantidade de mamadeiras: ")
    pedido = f"{nome_bebe} - {quantidade} mamadeira(s)"
    pedidos_mamadeiras.append(pedido)
    print(f"Pedido registrado: {pedido}\n")

def solicitar_remedio():
    """Solicita um remédio para um bebê."""
    nome_bebe = input("Digite o nome do bebê: ")
    remedio = input("Digite o nome do remédio: ")
    pedido = f"{nome_bebe} - {remedio}"
    pedidos_remedios.append(pedido)
    print(f"Pedido de remédio registrado: {pedido}\n")

def chamar_enfermeira():
    """Solicita a presença de uma enfermeira ou médico."""
    motivo = input("Digite o motivo para chamar a enfermeira ou médico: ")
    print(f"Chamando a enfermeira/médico... Motivo: {motivo}\n")

def listar_pedidos():
    """Lista todos os pedidos pendentes de mamadeiras e remédios."""
    if pedidos_mamadeiras or pedidos_remedios:
        print("Pedidos pendentes:")
        for i, pedido in enumerate(pedidos_mamadeiras, 1):
            print(f"Mamadeira {i}: {pedido}")
        for i, pedido in enumerate(pedidos_remedios, 1):
            print(f"Remédio {i}: {pedido}")
        print()
    else:
        print("Nenhum pedido pendente.\n")


while True:
    print("\n--- Sistema Baby Kitchen ---")
    print("1. Solicitar mamadeira")
    print("2. Chamar enfermeira/médico")
    print("3. Solicitar remédio")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        solicitar_mamadeira()
    elif opcao == "2":
        chamar_enfermeira()
    elif opcao == "3":
        solicitar_remedio()
    elif opcao == "4":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida, tente novamente.\n")
