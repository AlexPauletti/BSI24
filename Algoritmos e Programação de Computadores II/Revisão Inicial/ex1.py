nums = []
par = []
impar = []
usu = 1

while usu > 0:
    usu = int(input("Informe o número que deseja adicionar à contagem. Digite zero para encerrar o input: "))
    if usu == 0:
        break

    nums.append(usu)

for a in nums:
    if a%2 == 0:
        par.append(a)

    else:
        impar.append(a)

parsoma = len(par)
imparsoma = len(impar)
print(f"Foi(ram) inserido(s) {parsoma} número(s) par(es) e {imparsoma} número(s) ímpar(es).")