#----------------------------------------------------
####code for the problem 4 in TSA final tset 
#### name:王于凯 student ID:2016110083
#----------------------------------------------------
import numpy as np
from sympy import *



##FW Step 1:
tf1 = 1
tf2 = 2
xn = [0,0]
yn = [0,0]
assign = 3000
#x = np.arange(1, 3000, 0.1)
#y = (1 + ( x / 1000 ) ** 2)
#z = 2 * ( 1 + ( (3000 - x) / 1000 )** 2)
n = 1
if tf1 < tf2:
    xn[0] = assign
else:
    xn[1] = assign

while True:
    ##FW Step 2:
    path1 = (1 + ( xn[0] / 1000 ) ** 2)
    path2 = 2 * ( 1 + ( xn[1] / 1000 )** 2)

    if path1 < path2:
        yn[0] = assign
    else:
        yn[1] = assign

    ##FW Step 3:
    a = symbols('a')
    combine1 = (1 - a) * xn[0] + a * yn[0]
    combine2 = (1 - a) * xn[1] + a * yn[1]
    b = solve((1 + ( combine1 / 1000 ) ** 2) * (-1 * xn[0] + yn[0]) + 2 * ( 1 + ( combine2 / 1000 )** 2)* (-1 * xn[1] + yn[1]),a)
    b[0] = float(b[0])
    print(b[0])
    xn_1 = xn[0]
    xn_2 = xn[1]
    xn[0] = (1 - b[0])*xn[0] + b[0]*yn[0]
    xn[1] = 3000 - xn[0]

    #FW Step 4:
    if xn_1 == 0 :
        pass
    elif abs((xn[0] - xn_1) / xn_1) < 0.003 :
        break
    if b[0] <= 0 or b[0] >= 1:
        xn[0] = xn_1
        xn[1] = xn_2
        break
    print(xn)
print("the final answer : x1 = {}  x2 = {}".format(xn[0], xn[1]))
