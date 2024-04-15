ano = int(input("Digite um ano: "))

if (ano%4 == 0 and ano%100 != 0):
    print("BISSEXTO")
else:
    if (ano%400 == 0):
        print("BISSEXTO")
    else:
        print("NÃO É BISSEXTO")