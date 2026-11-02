"""Exercício 5 - Investimento com juros compostos mês a mês."""


def ler_numero(mensagem, tipo=float):
    """Lê um número positivo do usuário, repetindo até ser válido."""
    while True:
        try:
            valor = tipo(input(mensagem).replace(",", "."))
            if valor > 0:
                return valor
        except ValueError:
            pass
        print("Valor inválido. Digite um número maior que 0.")


saldo = ler_numero("Digite o valor inicial para investimento R$: ")
taxa = ler_numero("Digite o valor da taxa de Juros (%) : ")
meses = ler_numero("Digite a quantidade de meses: ", int)

for mes in range(1, meses + 1):
    saldo += saldo * taxa / 100
    print(f"Mês {mes}: R${saldo:.2f}")