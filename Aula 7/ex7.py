cod = int(input("Informe o número de seu código: "))
salario = float(input("Informe o valor do seu salário: "))

if cod == 5:
    print("Seu cargo é de diretor e seu salário não receberá ajustes")

else:
    if cod == 4:
        print(f"Seu cargo é de Gerente, receberá um aumento de R${(salario/100)*10}, tornando seu novo salário R${salario + ((salario/100)*10)}")
    
    else:
        if cod == 3:
            print(f"Seu cargo é de Caixa, receberá um aumento de R${(salario/100)*20}, tornando seu novo salário R${salario + ((salario/100)*20)}")
        
        else:
            if cod == 2:
                print(f"Seu cargo é de Secretário, receberá um aumento de R${(salario/100)*35}, tornando seu novo salário R${salario + ((salario/100)*35)}")
            
            else:
                if cod == 1:
                    print(f"Seu cargo é de Escriturário, receberá um aumento de R${(salario/100)*50}, tornando seu novo salário R${salario + ((salario/100)*50)}")