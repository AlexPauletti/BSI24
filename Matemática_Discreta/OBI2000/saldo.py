quant = int(input("Quantas partidas foram realizadas pelo time? "))
historico = []
GA = [] #gols a favor
GC = [] #gols contra
aux = 0
saldo = 0
p1 = 0
aj1 = 0
aj2 = 0

print("Digite o primeiro número como gols a favor do time, e o segundo número como gols contra o time. Ex: 2 0")
for a in range(quant):
    partida = input("Informe os gols da partida: ")
    historico.append(partida)

for b in historico:
    gols = b.split(' ')
    GA.append(int(gols[0]))
    GC.append(int(gols[1]))
 
maior = GA[0] - GC[0]
cont = 0
cont2 = 1
for v in range(quant):
    p1 = GA[v] - GC[v]

    for f in range(quant):
        p2 = GA[cont2] - GC[cont2]

        if p1 + p2 > maior:
            aux = p1+p2

            if v == cont2:
                aux = p1
                maior = aux
                if p1 > maior:
                    aj1 = v+1
                    aj2 = v+1
                    saldo = (f"{aj1},{aj2}")
            
            else:
                maior = aux
                aj1 = v+1
                aj2 = cont2+1
                saldo = (f"{v+1},{cont2+1}")
        
        if p1 + p2 == maior:
            if cont2 - v > aj2 - aj1:
                aj1 = v+1
                aj2 = cont2+1



        cont2 += 1
        if cont2 >= len(GA):
            break

    cont2 = 1    


if aj1 + aj2 <= 0:
    print("nenhum")

else:
    print(aj1, aj2)