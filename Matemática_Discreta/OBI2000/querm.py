N = int(input("Quantos participantes estiveram na festa? "))
ingressos = []
vencedor = 0

for a in range(N):
    ingressos.append(int(input("Digite os números dos ingressos, em ordem de chegada: ")))


for b in range(N):
    if b+1 == ingressos[b]:
        vencedor = ingressos[b]

print(vencedor)