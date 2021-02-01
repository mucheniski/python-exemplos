lista = [34,29,27,28,35]
print(lista)

# O metodo sorted retorna uma lista ordenada que precisa ser atribuida a lista novamente
listaOrdenadaComSorted = sorted(lista)
print(lista)
print(listaOrdenadaComSorted)

# O metodo sort altera uma lista que já existe
lista.sort()
print(lista)

# Ordenar decrescente
lista.sort(reverse=True)
print(lista)

# Inverter os valores da lista mesmo sem ordenar, pegando do último para o primeiro
lista.reverse()
print(lista)