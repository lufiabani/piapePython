precoUnidade = float(input("DIGITE O PREÇO POR UNIDADE: "))

quantidade = float(input("DIGITE A QUANTIDADE: "))

valorPago = float(input("DIGITE O VALOR PAGO: "))

custoTotal = quantidade * precoUnidade

troco = valorPago - custoTotal

print ("QUANTIDADE DE ITENS: ", quantidade, "\nCUSTO TOTAL: ", custoTotal, "\nTROCO: ", troco)