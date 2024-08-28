# cálculo do imposto + bônus
salario = float(input("Informe o seu salário: "))
imposto = float((salario/100)*7)
gratificacao = float((salario/100)*5)

print(f"O seu salário, com o imposto e sua gratificação já aplicadas, equivale a: {salario + gratificacao - imposto}")

