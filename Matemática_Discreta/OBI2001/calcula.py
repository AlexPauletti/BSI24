nums = []
sinais = []
resultado = 0

#pois é
print("use apenas numerais de um dígito")
quant = int(input("Quantos números serão usados na operação? "))
tome = input("Informe a operação: ")

quant = quant + (quant-1)

caracteres = list(tome)
cont = 0
cont2 = 1
for a in range(quant):
    if cont >= len(caracteres):
        break
    nums.append(int(caracteres[cont]))
    cont += 2

    if cont2 >= len(caracteres):
        break
    sinais.append(caracteres[cont2])
    cont2 += 2

print(sinais, nums)

if sinais[0] == "+":
    resultado = nums[0] + nums[1]
    del nums[0]
    del nums[0]
    del sinais [0]

elif sinais[0] == "-":
    resultado = nums[0] - nums[1]
    del nums[0]
    del nums[0]
    del sinais [0]    

while len(nums) > 0:
    if sinais[0] == "+":
        resultado + nums[0]
        del sinais[0]
        del nums[0]

    elif sinais[0] == "-":
        resultado - nums[0]
        del sinais[0]
        del nums[0]

print(resultado)    