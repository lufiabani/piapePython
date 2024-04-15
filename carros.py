carros = int(input("Digite o número de carros vendidos: "))
vendas = float(input("Digite o valor total de suas vendas: "))
fixo = float(input("Digite o salário fixo: "))

final = fixo + (300 * carros) + (0.05 * vendas)

print (final)