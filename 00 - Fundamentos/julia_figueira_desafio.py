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

    if opcao == "d":
        print("Depósito")
    
    elif opcao == "s":
        print("Saque")
    
    elif opcao == "e":
        print("Extrato")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

# Fim do programa