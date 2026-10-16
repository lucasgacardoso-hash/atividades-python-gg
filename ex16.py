saldo = float (input("Digite o saldo da conta: "))
sacar = float (input ("Digite o valor que você deseja sacar: "))

if sacar >saldo:
    print("Saldo insuficiente")
else:
    print("Saque realizado. novo saldo :",saldo-sacar)