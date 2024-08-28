quant_pao = int(input("Informe a quantidade de pães vendidos: "))
quant_broa = int(input("Informe a quantidade de broas vendidas: "))

rendimento_pao = (quant_pao*0.50)
rendimento_broa = (quant_broa*1.50)

rendimento_total = (rendimento_pao + rendimento_broa)
poupanca = ((rendimento_total/100)*10)

print(f"O rendimento de vendas dos pães e broas de hoje equivale a {rendimento_total}")
print(f"O valor que deverá ser guardado para poupança é {poupanca}")