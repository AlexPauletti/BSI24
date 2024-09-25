import numpy as np

X = 2
Y = 4
VL = [2, 6, 8, 3, 10, 9, 1, 21, 33, 14]

V = np.array(VL)

print(
V[X+1],
V[X+2],
V[X+3],
V[X*4],
V[X*1],
V[X*2],
V[X*3],
V[V[X+Y]],
V[X+Y],
V[8-V[2]],
#V[V[4]], <--- Vai dar erro, pois o array não possui index 10
#V[V[V[7]]], <--- Vai dar erro, pois o array não possui index 21
#V[V[1]*V[4]], <--- Vai dar erro, pois o array não possui index 60
V[X+4],
)

