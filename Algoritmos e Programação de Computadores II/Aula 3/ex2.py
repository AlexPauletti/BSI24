A = set()
R = set()

for a in range(5):
    receba = int(input("Informe os números vencedores da LOTO: "))
    R.add(receba)

for b in range(10):
    receba2 = int(input("Informe o número que queira apostar na LOTO: "))
    A.add(receba2)


pontos = len(A & R)
print(pontos)