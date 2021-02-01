listaNumeros = [1,2,3,4,5]

# Lista ao quadrado da lista original
# listaAoQuadrado = [valor_a_adicionar laco]
# i**2 i elevado a segunda potência
listaAoQuadrado = [i**2 for i in listaNumeros]

# Lista com a condição, apenas os impares da lista original, pegando o resto da divisão por dois
# listaComCondicao = [valor_a_adicionar laco condicao]
listaComCondicao = [i for i in listaNumeros if i % 2 == 1]


print("Usando list comprehension")
print(listaNumeros)
print(listaAoQuadrado)
print(listaComCondicao)

