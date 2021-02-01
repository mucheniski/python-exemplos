textoExemplo = " Bruna Lindeza Linda "

minusculo = textoExemplo.lower()
print(minusculo)

maiusculo = textoExemplo.upper()
print(maiusculo)

# Remover espaços no inicio e fim e caracteres especiais
semEspacosECaracteres = textoExemplo.strip()
print(semEspacosECaracteres)

# Converte o texto em uma lista
lista = textoExemplo.split()
print(lista)

# Separa a lista com quebra por letra
listaQuebrada = textoExemplo.split("a")
print(listaQuebrada)

# Busca de substring, se não encontra retorna -1
posicaoPalavra = textoExemplo.find("Lindeza")
print(posicaoPalavra)

# Imprime só o que vem depois da busca
posicaoDepois = textoExemplo[posicaoPalavra:]
print(posicaoDepois)

# Substituir partes da string
textoSubstituido = textoExemplo.replace("Lindeza", "Gata")
print(textoSubstituido)