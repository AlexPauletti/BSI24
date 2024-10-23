import numpy as np

S = np.zeros(10)
R = np.zeros(5)
XL = []

for a in range(10):
    S[a] = int(input("Informe o número que vai adicionar ao Vetor S: "))

for b in range(5):
    R[b] = int(input("Informe o número que vai adicionar ao Vetor R: "))


for c in S:
    for d in R:
        if d == c:
            XL.append(d)
            

sizeL = len(XL)
X = np.array(XL)

if sizeL > 0:
    print("Os números em comum entre os arrays S e R são: ")
    for e in range(sizeL):
        print(X[e])

else:
    print("Não há números em comum entre os dois arrays.")