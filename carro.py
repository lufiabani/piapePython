ano = int(input("Digite o ano do carro: "))
valor = float(input("Digite o valor da tabela do carro: "))

if (ano < 2000):
    total = valor + valor * 0.01
else:
    total = valor + valor * 0.015

print (total)