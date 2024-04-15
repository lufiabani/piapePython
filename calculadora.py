n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
operacao = input("Digite a operação (+, -, /, *): ")

if (operacao == "+"):
    total = n1 + n2
elif (operacao == "-"):
    total = n1-n2
elif (operacao == "*"):
    total = n1*n2
else:
    if (n2 != 0):
        total = n1 / n2
    else:
        total = "ERRO - DIVISÃO POR ZERO"

print (total)