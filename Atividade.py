class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def get_numero(self):
        return self.numero

    def get_saldo(self):
        return self.saldo

    def debitar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def creditar(self, valor):
        self.saldo += valor

class Banco:
    def __init__(self):
        self.contas = [None] * 100
        self.indice = 0

    def cadastrar(self, conta: Conta):
        self.contas[self.indice] = conta
        self.indice += 1

    def procurar_conta(self, numero):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1
        if achou is True:
            return self.contas[i]
        else:
            return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta Inexistente!")

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta Inexistente!")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("Conta Inexistente!")
            return None

    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)
        if conta_origem and conta_destino:
            if conta_origem.get_saldo() >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print(f"Transferência de R$ {valor} realizada com sucesso de conta {origem} para conta {destino}.")
            else:
                print("Saldo insuficiente na conta de origem!")
        else:
            print("Conta de origem ou destino inexistente!")

# Programa principal para testar as classes
if __name__ == "__main__":
    banco = Banco()


    conta1 = Conta(123, 1000)
    conta2 = Conta(456, 500)
    conta3 = Conta(789, 200)


    banco.cadastrar(conta1)
    banco.cadastrar(conta2)
    banco.cadastrar(conta3)


    print(f"Saldo da conta 123: R$ {banco.saldo(123)}")
    print(f"Saldo da conta 456: R$ {banco.saldo(456)}")
    print(f"Saldo da conta 789: R$ {banco.saldo(789)}")


    banco.creditar(123, 200)
    print(f"Saldo da conta 123 após crédito de R$ 200: R$ {banco.saldo(123)}")


    banco.debitar(456, 100)
    print(f"Saldo da conta 456 após débito de R$ 100: R$ {banco.saldo(456)}")


    banco.transferir(123, 789, 300)
    print(f"Saldo da conta 123 após transferência: R$ {banco.saldo(123)}")
    print(f"Saldo da conta 789 após transferência: R$ {banco.saldo(789)}")


    banco.creditar(999, 50)  # Deve imprimir "Conta Inexistente!"
    banco.saldo(999)  # Deve imprimir "Conta Inexistente!" e retornar None
