print(True and True and True)
print(True and False and True)
print(True or True and False)
print(True or False)
print(False or False)

print("================================")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_nomral_com_saldo_suficiente = saldo >= saque and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_nomral_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

