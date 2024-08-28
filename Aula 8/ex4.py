X = float(input("Informe o valor de X: "))
Y = float(input("Informe o valor de Y: "))

soma = X + Y

porce = (soma/100 * 30)

if porce > 500:
    tome = X
    X = Y
    Y = tome

    print(f"X = {X}, Y = {Y}")

else:
    if X < Y:
        print(f"O menor valor é {X}")

    else:
        if Y < X:
            print(f"O menor valor é {Y}")
