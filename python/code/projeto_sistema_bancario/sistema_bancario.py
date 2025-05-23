menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 100
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é invalido.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor de saque:"))

        if valor <= 0:
            print("Operação invalida! O valor informado e invalido.")

        elif valor > saldo:
            print("Operação falhou! O valor excede o limite de saque.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Numero maximo de saques excedido.")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")
            print("Retire o dinheiro!")

    elif opcao == "e":
        print("\n================== EXTRATO ==================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a opreação desejada.")
