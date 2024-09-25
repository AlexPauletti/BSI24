#simulador de tigrinho
import numpy as np

A = np.zeros(10)
R = np.zeros(5)
XL = []

for a in range(5):
    R[a] = int(input("Informe os 5 números vencedores da LOTO: "))

for b in range(10):
    A[b] = int(input("Informe 10 números que queira apostar na LOTO: "))


for c in A:
    for d in R:
        if d == c:
            XL.append(d)
            

sizeL = len(XL)
X = np.array(XL)

if sizeL > 0:
    print(f"Você fez {sizeL} ponto(s)")

else:
    print("Você não fez pontos.")