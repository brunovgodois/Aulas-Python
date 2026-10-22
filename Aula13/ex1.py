veiculos = ['Ferrari F40', 'Ferrari SF90 Stradale', 'Porsche Carrera GT', 'Porsche 918 Spyder', 'Mercedes SLR']

# Acessar elementos da lista
# Acesso rápido: lista[indice]
# O índice de uma lista inicia em 0

# Recuperar e alterar valores
print(veiculos[0])

veiculo = veiculos[3]
print(veiculo)

# Alterando um elemento da lista
veiculos[1] = 'Ferrari SF90 Stradale'
print(veiculos[1])          

# Exibindo todos os elementos da lista
print(veiculos)

# Trocando a ordem dos elementos das posições 1 e 2
veiculo1 = veiculos[1]
veiculo2 = veiculos[2]
veiculos[1] = veiculo2
veiculos[2] = veiculo1

print(veiculos)

# Acesso posicional
# For-Each
print("Percorrendo uma lista com For-Each: ")
i = 0                       
for item in veiculos:
    print(f"{i} : {item}")
    i += 1                  

# Ou

# Obter o tamanho da lista
print("Tamanho da lista é: ", len(veiculos))  

# Ou

# For com range
print("Percorrendo uma lista com for: ")
# for necessita de variavel  i para percorrer na lista
for i in range(len(veiculos)):
    print(f"{i} : {veiculos[i]}")   
    # i: índice

#Ou

# While
ii = 0
print("Percorrendo uma lista com while: ")
while ii < len(veiculos):
    print(f"{ii} : {veiculos[ii]}")
    ii += 1