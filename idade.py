idade = int(input("Digite sua idade: "))

if(idade < 18):
    print ("menor de idade")
else:
    if (idade > 65):
        print("idoso")
    else:
        print("adulto")