
saldo = 0
extrato = []
LIMITE_SAQUES = 3
saques_realizados = 0

while True:
    print("\n===== SISTEMA BANCÁRIO =====")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido.")

    elif opcao == "2":
        valor = float(input("Valor do saque: R$ "))

        if valor <= 0:
            print("Valor inválido.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif saques_realizados >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        else:
            saldo -= valor
            saques_realizados += 1
            extrato.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")

    elif opcao == "3":
        print("\n===== EXTRATO =====")

        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for movimentacao in extrato:
                print(movimentacao)

        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida. Tente novamente.")
