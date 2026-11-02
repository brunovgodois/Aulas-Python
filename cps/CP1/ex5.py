salario1 = float(input("Digite seu salario: "))

imposto = 0

if salario1 <= 2428.80:
    imposto = salario1 * 0 - 0

elif salario1 <= 2826.65:
    imposto = salario1 * 0.750 - 182.16

elif salario1 <= 3751.05:
    imposto = salario1 * 0.15 - 394.16

elif salario1 <= 4664.68:
    imposto = salario1 * 0.22 - 675.49

elif salario1 <= 4664.69:
    imposto = salario1 * 0.27 - 908.75

else:
    imposto = salario1 * 0.27 - 908.75

print(f"Você pagará: {imposto}")