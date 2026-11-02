salario = float(input("Salário: R$ "))
if salario <= 1621.00:
    aliquota = 0.075
    deducao = 0.00

elif salario <= 2902.84:
    aliquota = 0.09
    deducao = 24.32

elif salario <= 4354.27:
    aliquota = 0.12
    deducao = 111.40
    
else:
    aliquota = 0.14
    deducao = 198.49
inss = (salario * aliquota) - deducao
print(f"INSS R$ {inss:.2f}")




