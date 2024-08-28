cod = int(input("Informe o código do produto: "))

if cod == 1:
    print("Alimento não-perecível")

else:
    if cod == 2 or cod== 3 or cod == 4:
        print("Alimento perecível")

    else:
        if cod == 5 or cod == 6:
            print("Vestuário")

        else:
            if cod == 7:
                print("Higiene pessoal")

            else:
                if cod >= 8 and cod <= 15:
                    print("Limpeza e utensílios domésticos")

                else:
                    print("Inválido")

