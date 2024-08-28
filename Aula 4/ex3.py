valor = float(input("Informe o valor em pés que gostaria de converter: "))
v_polegadas = (valor*12)
v_jardas = round(valor/3, 2)
v_milhas = round(v_jardas/1760, 2)

print(f"Resultado do valor convertido em \n Polegadas: {v_polegadas} \n Jardas: {v_jardas} \n Milhas: {v_milhas}")