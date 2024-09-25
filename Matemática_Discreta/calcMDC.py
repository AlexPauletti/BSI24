
nums = []
asker = 0
mdc = 0
resto = 6
aux = 0
num1 = 0
num0 = 0

quantNums = int(input("Quantos números você gostaria de adicionar ao cálculo? "))

for a in range(quantNums):
    asker = int(input("Digite o número que queira adicionar: "))
    nums.append(asker)

while len(nums) != 0:
    if nums[1] > nums[0]:
        aux = nums[1]
        nums[1] = nums[0]
        nums[0] = aux

    num1 = nums[1]
    num0 = nums[0]
    while resto != 0:
        if num0%num1 == 0:
            mdc = num1

            del nums[0]
            del nums[0]

            if len(nums) > 0:
                nums.insert(0, num1)
            break
            
        resto = num0%num1   
                
        num0 = num1
        num1 = resto

print(f"O MDC desses números é {mdc}.")