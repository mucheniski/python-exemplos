# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite o sinal da operação: ")
calculo = 0

if operacao ==  "+":
    calculo = n1 + n2
elif operacao == "-":
    calculo = n1 - n2
elif operacao == "*":
    calculo = n1 * n2
elif operacao == "/":
    calculo = n1 / n2

print(calculo)