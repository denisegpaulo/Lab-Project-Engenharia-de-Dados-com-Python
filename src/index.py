
# Definição do Menu na tela do caixa eletrônico
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
# Inicialização das Variáveis
saldo = 0                # Armazena o saldo inicial, que começa em 0.
limite = 2500            # Define o valor máximo permitido para um saque
extrato = ""             # Armazena o histórico das transações realizadas, começando como uma string vazia.
numero_saques = 0        # Conta quantos saques já foram realizados, iniciando em 0
LIMITE_SAQUES = 5        # Define o número máximo de saques permitidos, configurado como 5.


#Início do Loop Infinito
while True:

    opcao = input(menu)  # Entrada da Opção do Usuário

    if opcao == "d":     #Verificação das Opções do Usuário
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")