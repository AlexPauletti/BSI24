valor_c = float(input("Informe o valor de fábrica do veículo: "))
lucros = float(input("Informe o percentual de lucro do distribuidor: "))
imposto = float(input("Informe o percentual de imposto: "))

lucros_c = round(((valor_c/100) * lucros), 2)
imposto_c = round(((valor_c/100) * imposto), 2)

print(f"O preço total do veículo somando R${lucros_c} de lucro para o distribuidor e R${imposto_c} de imposto é de R${valor_c+imposto_c+lucros_c}")

