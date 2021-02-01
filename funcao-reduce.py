from functools import reduce

def soma(n1, n2):
    return n1 + n2

listaNumeros = [1, 2, 3, 4, 5]

# Executa a função para cada elemento da lista
# Recebe reduce(funcao, lista)
somaValores = reduce(soma, listaNumeros)

print(somaValores)