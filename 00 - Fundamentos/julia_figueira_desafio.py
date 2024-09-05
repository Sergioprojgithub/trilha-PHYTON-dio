# Criando o menu 
menu = """
########## MENU ##############

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

##############################
=> """

# Declarar variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Inicio do programa
while True:

    opcao = input(menu)

    # Operação de depósito
    if opcao == "d":
        print("Depósito")
        
        deposito = float(input("Informe o valor do depósito: "))
        
        if deposito > 0: 
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        
        else:
            print("Falha na operação! O valor informado é inválido.")
    
    #Operação de saque
    elif opcao == "s":
        print("Saque")
        saque = float(input("Informe o valor do saque: "))

        if saque > saldo:
            print("Falha na operação! Saldo insuficiente.")
        
        elif saque > limite:
            print(f"Falha na operação! O valor máximo por saque é de R$ {limite:.2f}")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Falha na operação! Limite de saques foi excedido.")

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")
    
    # Operação de extrato
    elif opcao == "e":       

        if extrato is "":
            print(f"""
            ================ EXTRATO ================
            Nenhuma movimentação foi realizada.
            Saldo: R$ {saldo:.2f}
            =========================================      
            """)
        
        else:    
            print(f"""
            ================ EXTRATO ================
            {extrato}
            Saldo: R$ {saldo:.2f}
            =========================================      
            """)    
            
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

# Fim do programa