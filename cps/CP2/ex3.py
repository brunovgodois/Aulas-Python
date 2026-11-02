"""Exercício 3 - Somatória e média de números inteiros positivos (0 encerra)."""

soma = 0
quantidade = 0

while True:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Valor inválido. Digite um número inteiro positivo.")
        continue

    if numero == 0:
        break
    if numero < 0:
        print("Valor inválido. Digite um número inteiro positivo.")
        continue

    soma += numero
    quantidade += 1

media = soma / quantidade if quantidade > 0 else 0

print(f"Somatória: {soma}")
print(f"Média: {media:g}" if media == int(media) else f"Média: {media:.2f}")