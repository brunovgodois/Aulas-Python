"""Exercício 2 - Tabuada de 1 a 10."""

while True:
    try:
        numero = int(input("Digite um número [1 até 10]: "))
    except ValueError:
        print("Valor fora do intervalo. É apenas aceito de 1 até 10")
        continue

    if 1 <= numero <= 10:
        break
    print("Valor fora do intervalo. É apenas aceito de 1 até 10")

for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")