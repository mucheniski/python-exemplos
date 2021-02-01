listaNumeros = [1,2,3,4,5]
listaAnimais = ["leao", "cachorro", "dinossauro", "elefante", "dragao"]
listaPeso = [400, 50, 6000, 2000, 5000]

# Função zip concatena as listas
# zip(lista1, lista2...)
for numero, animal, peso in zip(listaNumeros, listaAnimais, listaPeso):
    print(numero, animal, peso)