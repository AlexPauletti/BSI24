v1 = int(input("Informe o primeiro valor que queira comparar: "))
v2 = int(input("Informe o segundo valor: "))
v3 = int(input("Informe o terceiro valor: "))

maior = v1
menor = v1

if v2 > maior:
    maior = v2

if v3 > maior:
    maior = v3

if v2 < menor:
    menor = v2

if v3 < menor:
    menor = v3

print(f"O menor número entre os três é {menor} e o maior {maior}")