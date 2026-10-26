
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")

    return saldo, extrato


def sacar(saldo, valor, extrato, numero_saques):
    limite_saques = 3
    limite_saque = 500

    if valor <= 0:
        print("Valor inválido.")
    elif valor > limite_saque:
        print("O valor máximo por saque é R$ 500,00.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print("Saque realizado com sucesso!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")

    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)

    print(f"Saldo atual: R$ {saldo:.2f}")


def main():
    saldo = 0
    extrato = []
    numero_saques = 0

    while True:
        print("\n===== SISTEMA BANCÁRIO =====")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo, valor, extrato, numero_saques
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "0":
            print("Obrigado por utilizar nosso sistema!")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
