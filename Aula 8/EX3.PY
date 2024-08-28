A = float(input("Informe o primeiro valor: "))
B = float(input("Informe o segundo valor: "))
C = float(input("Informe o terceiro valor: "))
D = float(input("Informe o quarto valor: "))
E = float(input("Informe o quinto valor: "))

maior = A
if B > maior:
    maior = B

if C > maior:
    maior = C

if D > maior:
    maior = D

if E > maior:
    maior = E

print(f"O maior valor apresentado é {maior}")