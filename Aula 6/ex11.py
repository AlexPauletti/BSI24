v = float(input("Informe o valor da compra: "))

if v >= 50:
    print(f"Você obteve um lucro de R${(v/100) * 30}")

else: 
    if v > 29:
        print(f"Você obteve um lucro de R${(v/100) * 40}")

    else:
        if v > 9:
            print(f"Você obteve um lucro de R${(v/100) * 50}")

        else:
            print(f"Você obteve um lucro de R${(v/100) * 70}")    

