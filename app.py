class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if valor > 0:
            if len(self.saques) < 3 and valor <= 500 and self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Não foi possível realizar o saque. Verifique o limite diário ou saldo disponível.")
        else:
            print("O valor do saque deve ser positivo.")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


# Exemplo de uso:
if __name__ == "__main__":
    conta = ContaBancaria()
    conta.deposito(1000.50)
    conta.saque(300.75)
    conta.deposito(500.30)
    conta.saque(200.25)
    conta.extrato()
