#RM 575296 BRUNO VIEIRA DE GODOIS
#RM 574269 GUSTAVO POLICARPO ROLIM

def mostrar_tabuada(numero):
    contador = 1

    while contador <= 10:
        print(numero, "x", contador, "=", numero * contador)
        contador = contador + 1


numero = int(input("Digite um número [1 até 10]: "))

while numero < 1 or numero > 10:
    print("Valor fora do intervalo. É apenas aceito de 1 até 10")
    numero = int(input("Digite um número [1 até 10]: "))

mostrar_tabuada(numero)