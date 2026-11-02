#RM 575296 BRUNO VIEIRA DE GODOIS
#RM 574269 GUSTAVO POLICARPO ROLIM

placas = []
tipos = []
faturamento = 0


def registrar_entrada():
    placa = input("Digite a placa: ")

    if placa in placas:
        print("Veículo já registrado.")
    else:
        print("1 - Carro")
        print("2 - Moto")
        print("3 - Caminhonete")
        tipo = int(input("Digite o tipo do veículo: "))

        while tipo < 1 or tipo > 3:
            print("Tipo inválido.")
            tipo = int(input("Digite o tipo do veículo: "))

        placas.append(placa)
        tipos.append(tipo)

        print("Entrada registrada com sucesso.")


def registrar_saida():
    global faturamento

    placa = input("Digite a placa: ")
    posicao = -1
    contador = 0

    while contador < len(placas):
        if placas[contador] == placa:
            posicao = contador

        contador = contador + 1

    if posicao == -1:
        print("Veículo não encontrado.")
    else:
        horas = int(input("Digite a quantidade de horas: "))

        while horas <= 0:
            print("Digite uma quantidade de horas maior que zero.")
            horas = int(input("Digite a quantidade de horas: "))

        if tipos[posicao] == 1:
            subtotal = horas * 8
        elif tipos[posicao] == 2:
            subtotal = horas * 5
        else:
            subtotal = horas * 12

        if horas <= 2:
            desconto = 0
        elif horas <= 5:
            desconto = subtotal * 0.05
        else:
            desconto = subtotal * 0.10

        total = subtotal - desconto
        faturamento = faturamento + total

        print("Subtotal da estadia R$ %.2f" % subtotal)
        print("Desconto aplicado R$ %.2f" % desconto)
        print("Total a pagar R$ %.2f" % total)

        placas.pop(posicao)
        tipos.pop(posicao)


def mostrar_faturamento():
    print("Faturamento total acumulado: R$ %.2f" % faturamento)


opcao = 0

while opcao != 4:
    print("\n------ MENU ------")
    print("1 - Registrar entrada")
    print("2 - Registrar saída")
    print("3 - Ver faturamento")
    print("4 - Encerrar")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        registrar_entrada()
    elif opcao == 2:
        registrar_saida()
    elif opcao == 3:
        mostrar_faturamento()
    elif opcao == 4:
        mostrar_faturamento()
        print("Sistema encerrado.")
    else:
        print("Opção inválida.")