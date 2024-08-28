saco = float(input("Informe o peso em quilos do saco de ração: "))
comida = float(input("Informe quantas gramas de ração é proporcionada aos gatos: "))

d5_comida = round(((comida*2)/1000) * 5, 2)

print(f"Daqui a 5 dias restará {saco-d5_comida} quilos de ração")