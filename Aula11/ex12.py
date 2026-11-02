# Gerenciar Aluno
# 1 - Cadastrar
# 2 - Consultar
# 3 - Atualizar
# 4 - Remover
# 5- Listar Alunos
# 6 - Sair do programa

while True:
    print("Gerenciar Aluno")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Atualizar")
    print("4 - Remover")
    print("5 - Listar Alunos")
    print("6 - Sair do programa")

    opcao = input("Digite uma opção: ")

    #Função isdigit(): utilizada para verificar se contém apenas numeros
    if opcao.isdigit():
        opcao = int(opcao)
        match opcao:
            case 1:
                print("Cadastrando aluno")
            case 2:
                print("Consultar aluno")
            case 3:
                print("Remover aluno")
            case 4:
                print("Remover aluno")
            case 5:
                print("Listar os alunos")
            case 6:
                print("Saindo do programa")
                break
            case _:
                print("Você digitou uma opção invalida! Tente novamente")

    else:
        print("Digite apenas numero de 1 até 6")