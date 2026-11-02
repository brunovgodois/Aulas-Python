"""Exercício 6 - Fechamento de caixa de uma loja."""

LIMITE_DESCONTO_MAIOR = 500.00
DESCONTO_MAIOR = 0.15
DESCONTO_MENOR = 0.05


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


faturamento_total = 0.0

while True:
    print("\n------ MENU ---------")
    print("1 - Registrar nova venda")
    print("2 - Fechar o Caixa")
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("\n-- Registrar nova venda --")
        quantidade = ler_numero("Digite a quantidade de itens diferentes: ", int)

        subtotal = 0.0
        for item in range(1, quantidade + 1):
            subtotal += ler_numero(f"Digite o preço do item {item} R$: ")

        if subtotal > LIMITE_DESCONTO_MAIOR:
            desconto = subtotal * DESCONTO_MAIOR
        else:
            desconto = subtotal * DESCONTO_MENOR
        total_venda = subtotal - desconto
        faturamento_total += total_venda

        print(f"Subtotal da Venda R$ {subtotal:.2f}")
        print(f"Desconto aplicado R$ {desconto:.2f}")
        print(f"Total da Venda R$: {total_venda:.2f}")

    elif opcao == "2":
        print(f"\nFaturamento Total Acumulado: R${faturamento_total:.2f}")
        break

    else:
        print("Opção inválida. Digite 1 ou 2.")