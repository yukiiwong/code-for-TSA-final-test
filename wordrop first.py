import numpy as np
from sympy import *
import matplotlib.pyplot as plt


x = np.arange(1, 5000, 1)
#x = symbols('x') #求导时使用
y = (1 + ( x / 1000 ) ** 2)
z = 2 * ( 1 + ( (3000 - x) / 1000 )** 2)
m = x * y + (3000 - x)*z
#diffm = diff(m, x) #求m对x的导数
#求导结果
#3*x**2/1000000 + (-x + 3000)*(x/250000 - 3/250) - 2*(-x/1000 + 3)**2 - 1
#wardorp first principle
#x = symbols('x')
x_a = np.arange(0, 3000, 0.01)
inte1 = []
#inte = sympy.integrate((1 + ( x / 1000 ) ** 2),(x))
#x**3/3000000 + x
inte2 = []
#inte = sympy.integrate(((2 * ( 1 + ( (3000 - x) / 1000 )** 2), x)))
#x**3/1500000 + 2*x

for i in x_a:
    inte1.append(i**3/3000000 + i)
    inte2.append((3000 - i)**3/1500000 + 2*(3000 - i))

crossover = 10000000000
for i in range(len(inte2)):
    distance = (inte1[i] + inte2[i])
    if distance <= crossover:
        crossover = distance
        x_point = (i+1)*0.01
        y_point = distance

print(x_point, y_point)
    
