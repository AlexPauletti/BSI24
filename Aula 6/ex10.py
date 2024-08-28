idade = int(input("Informe sua idade: "))

if idade > 18:
    print("Você está na categoria Sênior")

else:
    if idade > 13:
        print("Você está na categoria Juvenil B")
    else:
        if idade > 10:
            print("Você está na categoria Juvenil A")
        else:
            if idade > 7:
                print("Você está na categoria Infantil B")
            else:
                if idade > 4:
                    print("Você está na categoria Infantil A")
                else:
                    print("Você não tem idade para participar")