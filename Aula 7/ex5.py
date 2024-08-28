salario = float(input("Informe seu salário: "))
c1 = float(input("Informe o valor da primeira conta: "))
c2 = float(input("Informe o valor da segunda conta: "))

salario = salario - (c1+((c1/100)*2)) - (c2+((c2/100)*2))

if salario > 0:
    print(f"Resta R${salario} de seu salário")

else:
    if salario == 0:
        print("Sua conta está zerada")    
    else:
        if salario < 0:
            print(f"Sua conta está negativada, em um valor de R${salario}")