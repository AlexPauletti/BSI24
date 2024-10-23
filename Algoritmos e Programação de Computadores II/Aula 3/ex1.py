S = set()
R = set()

for a in range(10):
    receba = int(input("Informe o número que queira adicionar ao vetor S: "))
    S.add(receba)

for b in range(5):
    receba2 = int(input("Informe o número que queira adicionar ao vetor R: "))
    R.add(receba2)


print(S & R)