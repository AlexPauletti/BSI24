deposito = float(input("Informe seu investimento inicial: "))
juros = float(input("Infome a porcentagem da taxa de juros anual: "))
rendimento = ((deposito/100)*juros)

print(f"Você rendeu {rendimento} sobre seu depósito esse ano.")
print(f"O valor total de seu depósito agora é: {deposito + rendimento}")
