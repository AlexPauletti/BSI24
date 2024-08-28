sexo = input("Informe seu sexo (F ou M): ")
idade = int(input("Informe sua idade: "))

if sexo == "F":
    if idade <= 12:
        print("Você é uma menina")

    elif idade <= 24:
        print("Você é uma moça")    

    elif idade > 24:
        print("Você é uma mulher")

elif sexo == "M":
    if idade <= 12:
        print("Você é um menino")

    elif idade <= 24:
        print("Você é um rapaz")    

    elif idade > 24:
        print("Você é um homem")

else:
    print("Por favor, insira seus dados novamente")