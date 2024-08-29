menu = """

[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair

>> """

saldo = 0
numero_saques = 0
extrato = {
    "depositos": [],
    "saques": [],
}

def sacar(saldo, valor_saque, extrato):
    limite = 500
    LIMITE_SAQUES = 3
    global numero_saques

    if (valor_saque <= saldo):
        if (numero_saques < LIMITE_SAQUES):
            if (0 < valor_saque <= limite):
                resultado = f"Saque de R${valor_saque:.2f} efetuado com sucesso!"
                saldo -= valor_saque
                numero_saques += 1
                extrato["saques"].append(valor_saque)
            else:
                resultado = f"Não foi possível realizar o saque. Informe apenas valores positivos e inferiores a R$ {limite:.2f}."
        else:
            resultado = "Você atingiu o limite máximo de saques por dia. Tente novamente amanhã."
    else:
        resultado = "Você não possui saldo suficiente para realizar o saque."

    print(resultado)
    return saldo



def depositar(saldo, valor_deposito, extrato):
    if (valor_deposito > 0):
        resultado = f"Depósito de R${valor_deposito:.2f} efetuado com sucesso!"
        saldo += valor_deposito
        extrato["depositos"].append(valor_deposito)
    else:
        resultado = "Não foi possível realizar o depósito. Informe apenas valores positivos e válidos."

    print(resultado)
    return saldo


while True:
    opcao = int(input(menu))

    if (opcao == 1):
        valor = float(input("Digite o valor de saque:\n>> "))
        saldo = sacar(saldo, valor, extrato)

    elif (opcao == 2):
        valor = float(input("Digite o valor de depósito:\n>> "))
        saldo = depositar(saldo, valor, extrato)

    elif (opcao == 3):
        print(" EXTRATO ".center(48, "#"))
        if (extrato["depositos"]):
            print("Depósitos:", end=" ")
            print(
            ', '.join(f"R$ {valor:.2f}" for valor in extrato["depositos"])
            )

        else:
            print("Não foram realizadas movimentações de depósito.")


        if (extrato["saques"]):
            print("\nSaques:", end=" ")
            print(
            ', '.join(f"R$ {valor:.2f}" for valor in extrato["saques"])
            )
        else:
            print("Não foram realizadas movimentações de saques.")

        print(f"\nSaldo da conta: R$ {saldo:.2f}")
        print("#########".center(48, "#"))

    elif (opcao == 0):
        print("Você saiu do sistema.")
        break

    else:
        print("Opção inválida, tente novamente.")
