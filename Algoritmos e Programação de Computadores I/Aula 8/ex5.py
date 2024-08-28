fuel = input("Informe o combustível abastecido (A para álcool e G para gasolina): ")
litros = float(input("Informe quantos litros foram abastecidos: "))

precoG = 7.20
precoA = 6.50
valorC = 0
desconto = 0
total = 0

if fuel == "A":
    if litros <= 20:
        valorC = precoA * litros
        desconto = (valorC/100 * 3)
        total = valorC - desconto
        
        print(f"Total: R${total}")

    elif litros > 20:
        valorC = precoA * litros
        desconto = (valorC/100 * 5)
        total = valorC - desconto
        
        print(f"Total: R${total}")

elif fuel == "G":
    if litros <= 20:
        valorC = precoA * litros
        desconto = (valorC/100 * 4)
        total = valorC - desconto
        
        print(f"Total: R${total}")

    elif litros > 20:
        valorC = precoA * litros
        desconto = (valorC/100 * 6)
        total = valorC - desconto
        
        print(f"Total: R${total}")




