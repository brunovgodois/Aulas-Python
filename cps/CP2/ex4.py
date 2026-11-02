"""Exercício 4 - Perfil de 5 clientes por idade."""

TOTAL_CLIENTES = 5

maiores_ou_iguais_18 = 0
menores_18 = 0
maior_idade = -1
cliente_mais_velho = 0

for cliente in range(1, TOTAL_CLIENTES + 1):
    while True:
        try:
            idade = int(input(f"Digite a idade do Cliente [{cliente}] : "))
            if idade >= 0:
                break
        except ValueError:
            pass
        print("Idade inválida. Digite um número inteiro maior ou igual a 0.")

    if idade >= 18:
        maiores_ou_iguais_18 += 1
    else:
        menores_18 += 1

    if idade > maior_idade:
        maior_idade = idade
        cliente_mais_velho = cliente

print(f"Clientes com 18 anos ou mais: {maiores_ou_iguais_18}")
print(f"Clientes com menos de 18 anos: {menores_18}")
print(f"Cliente mais velho: Cliente [{cliente_mais_velho}] com {maior_idade}")