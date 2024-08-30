from datetime import datetime

menu = """

[1] DEPOSITAR
[2] SACAR
[3] VER EXTRATO
[4] CRIAR NOVO USUÁRIO
[5] CRIAR NOVA CONTA
[6] LISTAR USUÁRIOS EXISTENTES
[7] LISTAR CONTAS EXISTENTES
[0] SAIR

=> """

usuarios = []
contas = []

saldo = 0

transacoes = []

numero_saques = 0
limite = 500
LIMITE_SAQUES = 3

numero_transacoes = 0
LIMITE_TRANSACOES = 10

def verificador_usuario_existente(CPF, usuarios):
    cpfs = [usuarios["CPF"] for usuarios in usuarios]
    return CPF in cpfs

def buscar_usuario_por_CPF(CPF, usuarios):
    usuarios_buscados = [
        usuario for usuario in usuarios if usuario["CPF"] == CPF]

    return usuarios_buscados[0] if usuarios_buscados else None

def criar_usuario(nome, data_nascimento, CPF, endereco, usuarios):
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "CPF": CPF,
        "endereco": endereco,
        "contas": []
    }

    usuarios.append(usuario)

    print("\nOperação sucedida! Usuário cadastrado com sucesso!")

    return usuarios

def criar_conta_corrente(usuario, contas):
    AGENCIA = "0001"

    conta_corrente = {
        "agencia": AGENCIA,
        "numero_conta": len(contas) + 1,
        "usuario": {
            "nome": usuario["nome"],
            "data_nascimento": usuario["data_nascimento"],
            "CPF": usuario["CPF"],
            "endereco": usuario["endereco"],
        },
    }

    contas.append(conta_corrente)

    print(f"\nConta criada e vinculada ao CPF: {usuario["CPF"]} com sucesso!")

    return contas

def registrar_data_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def criar_transacao(tipo, quantia, data):
    transacao = {
        "tipo": tipo,
        "valor": quantia,
        "data": data
    }

    return transacao

def depositar(
        saldo, valor, transacoes, numero_transacoes, limite_transacoes, /):

    excedeu_transacoes = numero_transacoes >= limite_transacoes

    if excedeu_transacoes:
        print("Operação falhou! Número máximo de transações excedido.")

    elif valor > 0:
        data_atual = registrar_data_atual()
        saldo += valor
        transacao = criar_transacao("DEPÓSITO", valor, data_atual)
        transacoes.append(transacao)
        numero_transacoes += 1
        print(f"\nOperação sucedida! Valor depositado: R$ {valor:.2f}")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, numero_transacoes

def sacar(*, saldo, valor, transacoes, limite, numero_saques, limite_saques, numero_transacoes, limite_transacoes):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    excedeu_transacoes = numero_transacoes >= limite_transacoes

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif excedeu_transacoes:
        print("\nOperação falhou! Número máximo de transações excedido.")

    elif valor > 0:
        data_atual = registrar_data_atual()
        saldo -= valor
        transacao = criar_transacao("SAQUE", valor, data_atual)
        transacoes.append(transacao)
        numero_saques += 1
        numero_transacoes += 1
        print(f"\nOperação sucedida! Valor de saque: R$ {valor:.2f}")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, numero_saques, numero_transacoes

def exibir_transacoes(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not transacoes:
        print("\nNão foram realizadas movimentações.")
    else:
        for (i, transacao) in enumerate(extrato):
            print(f"\n{i+1}ª TRANSAÇÃO")
            print(f"-> Tipo: {transacao["tipo"]}")
            print(f"-> Valor: {transacao["valor"]:.2f}")
            print(f"-> Data e Hora: {transacao["data"]}")

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n==========================================")

def exibir_usuarios(usuarios):
    print("\n================ USUÁRIOS ================")
    for (i, usuario) in enumerate(usuarios):
        print(f"\n{i+1}º USUÁRIO")
        print(f"-> Nome: {usuario["nome"]}")
        print(f"-> Nascimento: {usuario["data_nascimento"]}")
        print(f"-> CPF: {usuario["CPF"]}")
        print(f"-> Endereço: {usuario["endereco"]}")
    print("\n==========================================")

def exibir_contas(contas):
    for conta in contas:
        print("\n================= CONTAS =================")
        for (i, conta) in enumerate(contas):
            print(f"\n{i+1}ª CONTA")
            print(f"-> Agência: {conta["agencia"]}")
            print(f"-> Número: {conta["numero_conta"]}")
            print(f"-> Usuário: {conta["usuario"]["nome"]}")
        print("\n==========================================")

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))
        saldo, numero_transacoes = depositar(
            saldo, valor, transacoes, numero_transacoes, LIMITE_TRANSACOES)

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        saldo, numero_saques, numero_transacoes = sacar(
            saldo=saldo,
            valor=valor,
            transacoes=transacoes,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
            numero_transacoes=numero_transacoes,
            limite_transacoes=LIMITE_TRANSACOES
        )

    elif opcao == 3:
        exibir_transacoes(saldo, extrato=transacoes)

    elif opcao == 4:

        nome = input(
            "Digite o nome de usuário: ")
        data_nascimento = input(
            "Digite a data de nascimento do usuário: ")
        CPF = input(
            "Digite o CPF do usuário: ")
        endereco = input(
            "Digite o endereço do usuário: ")

        usuario_existente = verificador_usuario_existente(CPF, usuarios)

        if usuario_existente:
            print(
            "\nOperação falhou! Já existe um usuário cadastrado com esse CPF.")
        else:
            usuarios = criar_usuario(
                       nome, data_nascimento, CPF, endereco, usuarios)

    elif opcao == 5:
        CPF_a_buscar = input("Digite o CPF do usuário: ")

        usuario = buscar_usuario_por_CPF(CPF_a_buscar, usuarios)

        if usuario:
            contas = criar_conta_corrente(usuario, contas)
        else:
            print("\nOperação falhou! O usuário não existe, não foi possível prosseguir com a criação da conta.")

    elif opcao == 6:
        if usuarios:
            exibir_usuarios(usuarios)
        else:
            print("\nNenhum usuário encontrado.")

    elif opcao == 7:
        if contas:
            exibir_contas(contas)
        else:
            print("\nNenhuma conta encontrada.")

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
