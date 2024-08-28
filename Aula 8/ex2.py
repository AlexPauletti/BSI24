A = float(input("Informe o primeiro valor: "))
B = float(input("Informe o segundo valor: "))
C = float(input("Informe o terceiro valor: "))

maior = A
if B > maior:
    maior = B

if C > maior:
    maior = C

menor = A
if B < menor:
    menor = B

if C < menor:
    menor = C

meio = 0
if A < maior and A > menor:
    meio = A

if B < maior and B > menor:
    meio = B

if C < maior and C > menor:
    meio = C

print(f"Os valores organizados em ordem crescente ficam: {menor}, {meio}, {maior}")