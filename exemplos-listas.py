listaFrutas = ["abacate", "banana", "limao"]
print(listaFrutas)

# Imprimir apenas um elemento pelo indice
print(listaFrutas[2])

# Navegar na lista
for item in listaFrutas:
    print(item)

# Ver o tamanho da lista
tamanho = len(listaFrutas)
print(tamanho)

# Inserir item na lista
listaFrutas.append("morango")
print(listaFrutas)

# Verificar se existe na lista
if "morango" in listaFrutas:
    print("Tem morango")

# Remover elementos da lista
del listaFrutas[2]
print(listaFrutas)

# Remover um range 
del listaFrutas[1:2]
print(listaFrutas)

# Limpar a lista
del listaFrutas[:]
print(listaFrutas)