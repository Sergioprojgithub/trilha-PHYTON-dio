from datetime import datetime

menu = """

[1] SACAR
[2] DEPOSITAR
[3] VER EXTRATO
[0] SAIR

>> """

saldo = 0
numero_saques = 0
LIMITE_SAQUES = 3
numero_transacoes = 0
LIMITE_TRANSACOES = 10
transacoes = []

def sacar(saldo, valor_saque, transacoes):
    limite = 500

    if (valor_saque <= saldo):
        if (0 < valor_saque <= limite):
            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            transacao = {
                "tipo": "SAQUE", "valor": valor_saque, "data": data_atual
            }
            transacoes.append(transacao)
            saldo -= valor_saque
            resultado = f"\nSaque de R${valor_saque:.2f} efetuado com sucesso!"
        else:
            resultado = f"\nNão foi possível realizar o saque. Informe apenas valores positivos e até R$ {limite:.2f}."
    else:
        resultado = "\nNão foi possível realizar o saque. Você não possui saldo suficiente para realizar o saque."

    print(resultado)

    return saldo

def depositar(saldo, valor_deposito, transacoes):
    if (valor_deposito > 0):
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        transacao = {
            "tipo": "DEPÓSITO", "valor": valor_deposito, "data": data_atual
        }
        transacoes.append(transacao)
        saldo += valor_deposito
        resultado = f"\nDepósito de R${valor_deposito:.2f} efetuado com sucesso!"
    else:
        resultado = "\nNão foi possível realizar o depósito. Informe apenas valores positivos e válidos."

    print(resultado)

    return saldo

def exibir_extrato(saldo, transacoes):
    print("\n####################### EXTRATO #######################")
    if (transacoes):
        for index, transacao in enumerate(transacoes):
            print(f'''
        {index+1}ª Transação
        -> Tipo: {transacao["tipo"]}
        -> Valor: R$ {transacao["valor"]:.2f}
        -> Data e Hora: {transacao["data"]}
        ''', end="\n")

    else:
        print("\nNão foram realizadas movimentações na conta.")

    print(f"\nSaldo da Conta: R$ {saldo:.2f}\n")
    print("#######################################################")

while True:
    opcao = int(input(menu))

    if (opcao == 1):
        if not (numero_saques < LIMITE_SAQUES):
            print(
                "\nNão foi possível realizar o saque. Você atingiu o número máximo de saques diários permitidos.")
        elif not (numero_transacoes < LIMITE_TRANSACOES):
            print("\nNão foi possível realizar o saque. Você atingiu o número máximo de transações diárias permitidas.")
        else:
            valor = float(input("\nDigite o valor de saque:\n>> "))
            saldo = sacar(saldo, valor, transacoes)
            numero_saques += 1
            numero_transacoes += 1

    elif (opcao == 2):
        if not (numero_transacoes < LIMITE_TRANSACOES):
            print("Não foi possível realizar o depósito. Você atingiu o número máximo de transações diárias permitidas.")
        else:
            valor = float(input("\nDigite o valor de depósito:\n>> "))
            saldo = depositar(saldo, valor, transacoes)
            numero_transacoes += 1

    elif (opcao == 3):
        exibir_extrato(saldo, transacoes)

    elif (opcao == 0):
        print("\nVocê saiu do sistema.")
        break

    else:
        print("\nOpção inválida, tente novamente.")
