gas_preco = float(input("Informe o valor atual da gasolina: "))
pagamento = float(input("Informe o valor que gostaria de abastecer: "))

litros_enchidos = round(pagamento/gas_preco)

print(f"Você abasteceu {litros_enchidos} litros")