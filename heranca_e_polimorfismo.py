class Conta:
    def __init__(self, numero, titular, saldo=0.0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def saldo(self):
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
        else:
            print("Saldo insuficiente!")

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

    def __str__(self):
        return ("Dados da Conta:\n"
                f"Numero: {self._numero}\n"
                f"Titular: {self._titular}\n"
                f"Saldo: {self._saldo:.2f}\n"
                f"Limite: {self._limite:.2f}")
    

class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor): 
        self._saldo += valor - 0.10


class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo


class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        print("----------------------------------------")
        print(f"Saldo inicial da conta ({conta._titular}): {conta.saldo():.2f}")
        self._saldo_total += conta.atualiza(self._selic)
        print(f"Saldo final da conta ({conta._titular}): {conta.saldo():.2f}")


if __name__ == '__main__':
    c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'Jose', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    print("=== Atualizacao Individual ===")
    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(f"Conta Comum - Saldo: {c.saldo():.2f}")
    print(f"Conta Corrente - Saldo: {cc.saldo():.2f}")
    print(f"Conta Poupanca - Saldo: {cp.saldo():.2f}")

    print("\n=== Teste __str__ ===")
    print(cc)

    print("\n=== Atualizador de Contas ===")
    adc = AtualizadorDeContas(0.01)
    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print(f"\nSaldo total de todas as contas: {adc.saldo_total():.2f}")