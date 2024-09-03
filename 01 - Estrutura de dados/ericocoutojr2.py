def menu():
    menu = (
        "\n"
        "=============== MENU ===============\n"
        "[D]epositar\n"
        "[S]acar\n"
        "[E]Extrato\n"
        "[N]ova conta\n"
        "[L]istar contas\n"
        "Novo [U]suário\n"
        "[F]inalizar\n"
        "\n"
        "=> "
    )
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n=== Operação falhou! O valor informado é inválido. ===")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n=== Operação falhou! Você não tem saldo suficiente. ===")

    elif excedeu_limite:
        print("\n=== Operação falhou! O valor do saque excede o limite. ===")

    elif excedeu_saques:
        print("\n=== Operação falhou! Número máximo de saques excedido. ===")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n=== Operação falhou! O valor informado é inválido. ===")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não há movimentações registradas." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Já existe usuário com esse CPF! ===")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n=== Usuário não encontrado. ===")


def listar_contas(contas):
    if not contas==[]:
        for conta in contas:
            linha = (
                f"Agência:\t{conta['agencia']}\n"
                f"C/C:\t\t{conta['numero_conta']}\n"
                f"Titular:\t{conta['usuario']['nome']}"
            )
            print("=" * 100)
            print(linha)
    else:
        print("=== Não há conta a ser listada. ===")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao in ["d","D"]:
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao in ["s","S"]:
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao in ["e","E"]:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao in ["u","U"]:
            criar_usuario(usuarios)

        elif opcao in ["n","N"]:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao in ["l","L"]:
            listar_contas(contas)

        elif opcao in ["f", "F"]:
            break

        else:
            print("Operação inválida, selecione uma opção entre [ ].")


main()
