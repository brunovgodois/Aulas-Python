#RM 575296 BRUNO VIEIRA DE GODOIS
#RM 574269 GUSTAVO POLICARPO ROLIM

def validar_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False


senha = input("Digite uma senha: ")

while validar_senha(senha) == False:
    print("Senha inválida.")
    senha = input("Digite uma senha: ")

print("Senha válida.")