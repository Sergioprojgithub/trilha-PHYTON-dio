menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

transacoes = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print("Depósito")
        deposito = float(input("Quanto deseja depositar? "))
        if deposito > 0:
            saldo += deposito
            print(f"Você depositou R${deposito:.2f}, seu saldo é de R${saldo:.2f}")
            transacoes.append(f"Depósito de R${deposito:.2f} efetuado!")
        else:
            print("Favor informar valor positivo.")
    elif opcao == 's':
        print("Saque")
        saque = float(input("Quanto deseja retirar? "))
        if numero_saques != LIMITE_SAQUES:
            if saque > saldo:
                print("Valor inválido!")
            else:
                if saque > 1000:
                    print("Limite por saque atingido.")
                elif saque > 0:
                    saldo -= saque
                    numero_saques += 1
                    print(f"Você sacou R${saque:.2f}, seu saldo agora é de R${saldo:.2f}")
                    transacoes.append(f"Saque de R${saque:.2f} efetuado!")
                else:
                    print("Valor inválido.")

        else:
            print("Limite de saques atingido.")

    elif opcao == 'e':
        print("Extrato")
        # for transacao in transacoes:
        extrato = transacoes
        print(extrato)
        print(f"Seu saldo é de R${saldo:.2f}")

    elif opcao == 'q':
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
