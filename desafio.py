menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor a ser depositado: "))

        if (valor < 0):
            print("O valor informado é inválido.")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada!")

    elif opcao == "s":
        if saldo <= 0:
            print("Sem saldo.")
        elif numero_saques < LIMITE_SAQUES:
            valor = float(input("Insira o valor do saque: "))

            if valor > limite:
                print(f"Operação não realizada. O valor excede o limite de R$ {limite:.2f} por saque.")
            elif valor > saldo:
                print(f"Operação não realizada. O valor é maior que o saldo disponível (R$ {saldo:.2f}).")
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print("Operação realizada!")
        else:
            print("O limite de saques diários foi atingido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")