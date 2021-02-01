n1 = 2
n2 = 0

# Quando a exceção é tratada o programa segue sua execução normalmente
try:
    print(n1/n2)
except:
    print("Não é permitido dividir por zero")

print(n1/n1)