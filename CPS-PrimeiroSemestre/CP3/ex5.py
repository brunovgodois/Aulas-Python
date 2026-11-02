#RM 575296 BRUNO VIEIRA DE GODOIS
#RM 574269 GUSTAVO POLICARPO ROLIM

quantidade_contratos = 0
total_acumulado = 0


def calcular_financiamento(valor, taxa, meses):
    saldo = valor
    mes = 1

    while mes <= meses:
        saldo = saldo + saldo * taxa / 100
        print("Mês", mes, ": R$ %.2f" % saldo)
        mes = mes + 1

    parcela = saldo / meses

    return [saldo, parcela]


def realizar_simulacao():
    global quantidade_contratos, total_acumulado

    valor = float(input("Digite o valor do empréstimo R$: "))

    while valor <= 0:
        print("O valor deve ser maior que zero.")
        valor = float(input("Digite o valor do empréstimo R$: "))

    taxa = float(input("Digite a taxa de juros (%): "))

    while taxa < 0:
        print("A taxa não pode ser negativa.")
        taxa = float(input("Digite a taxa de juros (%): "))

    meses = int(input("Digite a quantidade de meses: "))

    while meses <= 0:
        print("A quantidade de meses deve ser maior que zero.")
        meses = int(input("Digite a quantidade de meses: "))

    resultado = calcular_financiamento(valor, taxa, meses)

    print("Valor total financiado: R$ %.2f" % resultado[0])
    print("Valor de cada parcela: R$ %.2f" % resultado[1])

    quantidade_contratos = quantidade_contratos + 1
    total_acumulado = total_acumulado + resultado[0]


def consultar_contratos():
    print("Quantidade de contratos simulados:", quantidade_contratos)
    print("Valor total financiado acumulado: R$ %.2f" % total_acumulado)


opcao = 0

while opcao != 3:
    print("\n------ MENU ------")
    print("1 - Realizar nova simulação")
    print("2 - Consultar contratos realizados")
    print("3 - Encerrar sistema")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        realizar_simulacao()
    elif opcao == 2:
        consultar_contratos()
    elif opcao == 3:
        print("Sistema encerrado.")
    else:
        print("Opção inválida.")