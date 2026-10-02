
Total_Economizado = 0
Mes = 1

while Mes <= 3:
    Valor = float(input(f"Digite o valor a ser economizado no mes {Mes} R$:"))
    Total_Economizado = Total_Economizado + Valor  # acumulador

    Mes += 1  # contador

print("Parabéns! Você economizou", Total_Economizado)