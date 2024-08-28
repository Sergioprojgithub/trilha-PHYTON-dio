# Criando o menu interativo
menu = '''
############### MENU #######################
Escolha uma operação:
[d] Depósito
[s] Saque
[e] Extrato
[x] Sair
############################################
==>'''

# Declaração de variáveis e constantes
saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUES = 3

# Inicio
while True:
    opcao = input(menu) 

    # Operação depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: 
            print("Falha na operação! O valor informado é inválido.")
        
    # Operação saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        if valor > saldo:
            print("Falha na operação! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Falha na operação! O valor do saque ultrapassa o limite.")

        elif qtd_saques >= LIMITE_SAQUES:
            print("Falha na operação! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtd_saques += 1
        
        else:
            print("Falha na operação! O valor informado é inválido.")

    # Exibir o extrato
    elif opcao == "e":
        
        if extrato is "":
            print("""
            ################# EXTRATO ##################
            Não foram realizadas movimentações na conta.
            ############################################
            """)
        else: 
            print(f"""
            ################# EXTRATO ##################
            Movimentações:\n{extrato}
            \nSaldo: R$ {saldo:.2f}
            ############################################
            """)

    # Sair
    elif opcao == "x":
        break
        
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")

# Fim       

