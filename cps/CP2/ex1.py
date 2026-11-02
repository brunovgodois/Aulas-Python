while True:
    try:
        nota = float(input("Digite uma Nota [0 ate 10]: ").replace(",", "."))
    except ValueError:
        print("Nota inválida. É apenas aceito de 0 até 10")
        continue

    if 0 <= nota <= 10:
        print(f'Nota "{nota:g}" registrada com sucesso')
        break
    print("Nota inválida. É apenas aceito de 0 até 10")