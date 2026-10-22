pokemons = ['Pikachu', 'Mew', 'Abra',
            'Charmander', 'Dragonite', 'Lucario']


# append(valor): adiciona itens no fim da lista
print("append")

print(pokemons, len(pokemons))
pokemons.append("Mewtwo")
pokemons.append("Kyurem")
pokemons.append("Ho-oh")

print(pokemons, len(pokemons))
print()


# insert(indice, valor): adiciona um item em uma posição específica
print("insert")

pokemons.insert(1, "Gengar")

print(pokemons, len(pokemons))
print()


# extend([valor, valor, valor]): adiciona múltiplos itens
print("extend")

pokemons.extend(['Charizard', 'Lugia', 'Tyranitar'])

print(pokemons, len(pokemons))
print()


# pop(index): remove um item da lista com base no índice (remove o Abra)
print("pop")

pokemons.pop(3)

print(pokemons)
print()


# reverse(): inverte a ordem atual da lista
print("reverse")

pokemons.reverse()

print(pokemons)
print()


# sort(): ordena os valores da lista em ordem crescente (A-Z, 0-9, etc.)
print("sort")

pokemons.sort()

print(pokemons)
print()


# remove(valor): remove um item da lista com base no valor
print("remove")

pokemons.remove("Dragonite")

print(pokemons)
print()


# del lista[index]: remove um item pelo índice
print("del")

del pokemons[2]

print(pokemons)
print()


# clear(): limpa a lista
print("clear")

pokemons.clear()

print(pokemons)