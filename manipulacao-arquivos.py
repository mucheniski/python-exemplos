arquivo = open("C:\ws-developer\python\meuarquivo.txt")
print(arquivo)

# Exibir apenas uma linha
linha = arquivo.readline()
print("Uma linha " + linha)

# Exibir as linhas
linhas = arquivo.readlines()
print(linhas)

# Exibir tudo
texto_completo = arquivo.read()
print(texto_completo)

arquivo.close()

# Escrevendo um arquivo
arquivo2 = open("C:\ws-developer\python\meuarquivo2.txt", "a")
arquivo2.write("Arquivo gerado pelo python\n")
arquivo2.close()