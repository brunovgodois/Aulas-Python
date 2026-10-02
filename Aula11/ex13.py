
# Gerenciar Aluno
# 1 - Cadastrar
# 2 - Consultar
# 3 - Atualizar
# 4 - Remover
# 5 - Listar Alunos
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

    # Verifica se contém apenas números
    if opcao.isdigit():
        opcao = int(opcao)

        if opcao == 1:
            print("Cadastrando aluno")

        elif opcao == 2:
            print("Consultando aluno")

        elif opcao == 3:
            print("Atualizando aluno")

        elif opcao == 4:
            print("Removendo aluno")

        elif opcao == 5:
            print("Listando os alunos")

        elif opcao == 6:
            print("Saindo do programa")
            break

        else:
            print("Você digitou uma opção inválida! Tente novamente.")

    else:
        print("Digite apenas números de 1 até 6!")