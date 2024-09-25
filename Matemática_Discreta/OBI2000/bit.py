I = 0
J = 0
K = 0
L = 0
saque = [I, J, K, L]

V = int(input("Que valor você gostaria de sacar? "))

if V >= 50:
    I = V//50
    V = V-I*50

if V >= 10:
    J = V//10
    V = V-J*10
    
if V >= 5:
    K = V//5
    V = V-K*5
    
if V >= 1:
    L = V//1
    V = V-L*1

print(I, J, K, L)
