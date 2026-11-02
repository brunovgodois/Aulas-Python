nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))

media = (nota1 + nota2) / 2
if media >= 6.0:
    print(f"{media} Você foi aprovado ")

else:
    print(f"{media} Você foi reprovado ")