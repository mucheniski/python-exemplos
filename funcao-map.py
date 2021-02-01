from typing import List

def dobro(x):
    return x * 2

valores = [1, 2, 3, 4, 5]

# map recebe dois argumentos(funcao, lista)
valoresDobrados = map(dobro, valores)

for valor in valoresDobrados:
    print(valor)