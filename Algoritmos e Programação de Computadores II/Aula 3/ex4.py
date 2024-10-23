nums = []
primos = []
pos = []

for a in range(9):
    tome = int(input("Informe o número que queira adicionar: "))
    nums.append(tome)

fator = 0
for b in range(9):
    for c in range(1, nums[b]+1):
        if nums[b] % c == 0:
            fator += 1

    if fator == 2:
        primos.append(nums[b])
        pos.append(b)
    
    fator = 0



print(primos)
print(pos)
