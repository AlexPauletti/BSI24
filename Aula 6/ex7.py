velocidade = float(input("Informe a velocidade do carro: "))

multa = 5
v_multa = velocidade - 80

if velocidade > 80:
    print(f"Você estava acima do limite e foi multado. O valor da multa é de R${multa*v_multa}")
    