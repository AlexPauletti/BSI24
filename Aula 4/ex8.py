peso_comida = float(input("Informe o peso de sua refeiçâo em quilogramas: "))

peso_prato = 0.800
valor_quilo = 45

valor_pagamento = round(valor_quilo*(peso_comida-peso_prato))

print(f"Valor à pagar: {valor_pagamento}")
