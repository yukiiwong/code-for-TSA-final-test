import numpy as np
from sympy import *

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
    path1 = (1 + ( xn[0] / 1000 ) ** 2)
    path2 = 2 * ( 1 + ( xn[1] / 1000 )** 2)

    if path1 < path2:
        yn[0] = assign
    else:
        yn[1] = assign

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
    print(xn)
print(xn)

'''原积分求解步骤
    inte1 = []
    # inte = sympy.integrate((1 + ( x / 1000 ) ** 2),(x))
    # x**3/3000000 + x
    inte2 = []
    # inte = sympy.integrate(((2 * ( 1 + ( (x) / 1000 )** 2), x)))
    # x**3/1500000 + 2*x
    x_a = np.arange(0, 1, 0.00001)
    for i in x_a:
        combine1 = (1-i) * xn[0] + i * yn[0]
        combine2 = 3000 - combine1
        inte1.append(combine1 ** 3 / 3000000 + i)
        inte2.append(combine2 ** 3 / 1500000 + 2 * combine2)
    crossover = 10000
    for i in range(len(x_a)):
        distance = (inte1[i] + inte2[i])
        if distance <= crossover:
            crossover = distance
            x_point = (i) * 0.00001
            y_point = distance
'''
