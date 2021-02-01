meu_dicionario = {"Eu":"Diego","Lideza":"Bruna","Tissa":"Patricia"}

# Imprimir apenas um valor
print(meu_dicionario["Eu"])

# Imprimir todo o dicionario
print(meu_dicionario)

# Imprimir por navegação, chave e valor da chave
for chave in meu_dicionario:
    print(chave + ":" + meu_dicionario[chave])

# Retornar os itens, converte os dados em tupla, que são imutáveis
for i in meu_dicionario.items():
    print(i)


# Retornar apenas os valores
for i in meu_dicionario.values():
    print(i)

# Retornar apenas as chaves
for i in meu_dicionario.keys():
    print(i)