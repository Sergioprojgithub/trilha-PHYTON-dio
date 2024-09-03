from datetime import datetime
from abc import ABC, abstractmethod

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self,  conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_saque = conta.sacar(self.valor)
        if sucesso_saque:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_deposito = conta.depositar(self.valor)
        if sucesso_deposito:
            conta.historico.adicionar_transacao(self)

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def __str__(self):
#         return f"""
# {self.__class__.__name__.upper()}
# {[f'{chave}: {valor}' for chave,valor in self.__dict__.items()]}
# """
        contas_info = '\n'.join([f"\t     Conta {conta.agencia}-{conta.numero} - Saldo: R$ {conta.saldo:.2f}" for conta in self.contas])

        return f"""
        CLIENTE
        -> Nome: {self.nome}
        -> CPF: {self.cpf}
        -> Nascimento: {self.data_nascimento}
        -> Endereco: {self.endereco}
        -> Contas:
{contas_info or "\t     Nenhuma conta cadastrada"}
        """

class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def cpf(self):
        return self._cpf

class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo

        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print(f"\nOperação sucedida! Valor de saque: R$ {valor:.2f}")
            return True

        else:
            print("\nOperação falhou! O valor informado é inválido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\nOperação sucedida! Valor de depósito: R$ {valor:.2f}")
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        limite_saques = self._limite_saques
        limite = self._limite

        excedeu_limite_saques = numero_saques >= limite_saques
        excedeu_limite = valor > limite

        if excedeu_limite:
            print(f"\nOperação falhou! Você excedeu o valor máximo de saque. (R$ {limite:.2f})")

        elif excedeu_limite_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
            Agência: {self.agencia}
            Número: {self.numero}
            Titular: {self.cliente.nome}
        """

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return None

    if len(cliente.contas) == 1:
        return cliente.contas[0]

    print("\nEscolha a conta:")
    for i, conta in enumerate(cliente.contas):
        print(f"[{i}] Conta {conta.agencia}-{conta.numero} - Saldo: R$ {conta.saldo:.2f}")

    indice = int(input("Digite o número da conta desejada: "))

    if 0 <= indice < len(cliente.contas):
        return cliente.contas[indice]
    else:
        print("\nOpção inválida! Operação cancelada.")
        return None

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\nCliente criado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!")

def listar_contas(contas):
    print("\n================ CONTAS ================")
    if contas:
        for conta in contas:
            print(conta)
    else:
        print("\nNenhuma conta registrada.")
    print("\n========================================")

def listar_clientes(clientes):
    print("\n================ CLIENTES ================")
    if clientes:
        for cliente in clientes:
            print(cliente)
    else:
        print("\nNenhum cliente registrado.")
    print("==========================================")

def menu():
    menu = """

[1] DEPOSITAR
[2] SACAR
[3] VER EXTRATO
[4] CRIAR NOVO USUÁRIO
[5] CRIAR NOVA CONTA
[6] LISTAR CONTAS EXISTENTES
[7] LISTAR CLIENTES EXISTENTES
[0] SAIR

=> """

    return int(input(menu))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)

        elif opcao == 3:
            exibir_extrato(clientes)

        elif opcao == 4:
            criar_cliente(clientes)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            listar_clientes(clientes)

        elif opcao == 0:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()