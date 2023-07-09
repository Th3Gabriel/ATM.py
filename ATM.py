from time import sleep


class ATM:
    def __init__(self):
        self.saldo = 0

    def check_balance(self):
        return self.saldo

    def deposit(self, quantidade):
        self.saldo += quantidade
        return f"Depositado {quantidade}. Novo Saldo: {self.saldo}"

    def withdraw(self, quantidade):
        if self.saldo >= quantidade:
            self.saldo -= quantidade
            print("Retirando...")
            return f"Retirado {quantidade} Com Sucesso. Novo Saldo: {self.saldo}"
        else:
            return "Saldo Insufiente"


# Example usage:
atm = ATM()

print("=================================")
print("     Welcome to the ATM!         ")
print("=================================")
print("1. Olhar Saldo")
print("2. Depositar")
print("3. Retirar")
print("4. Sair")
print("=================================")


while True:
    opc = int(input("Escolha uma das opções (1-4): "))

    if opc == 1:
        saldo = atm.check_balance()
        print(f"Seu saldo é: {saldo}")

    elif opc == 2:
        quantidade = float(input("Quanto deseja depositar R$: "))
        result = atm.deposit(quantidade)
        print("Depositando...")
        sleep(3)
        print(result)

    elif opc == 3:
        quantidade = float(input("Quanto deseja retirar R$: "))
        result = atm.withdraw(quantidade)
        print("Retirando...")
        sleep(3)
        print(result)

    elif opc == 4:
        print("Obrigado por utilizar nosso ATM, Volte sempre!")
        break
    else:
        print("Opção invalida, Digite um numero de 1-4, Que se encaixe no seu desejo!!")