class ContaBancaria:
    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_SAQUE_DIARIO = 500

    def __init__(self):
        self._saldo = 0
        self._saques_realizados_hoje = 0

    def deposito(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if valor > 0:
            if self._saques_realizados_hoje < ContaBancaria.LIMITE_SAQUES_DIARIOS and valor <= ContaBancaria.LIMITE_SAQUE_DIARIO and self._saldo >= valor:
                self._saldo -= valor
                self._saques_realizados_hoje += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Não foi possível realizar o saque. Verifique o limite diário ou saldo disponível.")
        else:
            print("O valor do saque deve ser positivo.")

    def extrato(self):
        print("Extrato:")
        if self._saques_realizados_hoje == 0:
            print("Não foram realizadas movimentações hoje.")
        else:
            print("Saques realizados hoje:")
            print(f"Número de saques: {self._saques_realizados_hoje}")
        print(f"Saldo atual: R$ {self._saldo:.2f}")


if __name__ == "__main__":
    conta = ContaBancaria()

    while True:
        print("\n1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor_deposito = float(input("Digite o valor do depósito: "))
            conta.deposito(valor_deposito)
        elif opcao == 2:
            valor_saque = float(input("Digite o valor do saque: "))
            conta.saque(valor_saque)
        elif opcao == 3:
            conta.extrato()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Digite novamente.")
