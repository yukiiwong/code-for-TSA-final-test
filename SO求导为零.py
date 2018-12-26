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


####求导为零
dm = 3*x**2/1000000 + (-x + 3000)*(x/250000 - 3/250) - 2*(-x/1000 + 3)**2 - 1
crossover = 10000
for i in range(len(x)):
    distance = (dm[i] - 0)**2
    if distance <= crossover:
        crossover = distance
        x_point = i + 1
        y_point = dm[i]

print(x_point, y_point)
