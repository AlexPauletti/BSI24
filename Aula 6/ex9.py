peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura em cm: "))

alt_imc = altura/100
imc = peso/(alt_imc**2)

if imc >= 40:
    print("Você é morbidamente obeso")

if imc >= 30 and imc < 40:
    print("Você é obeso")

if imc >= 25 and imc < 30:
    print("Você é sobrepreso")

if imc >= 20 and imc < 25:
    print("Voce possui um peso normal")

if imc < 20:
    print("Você está abaixo do peso")
