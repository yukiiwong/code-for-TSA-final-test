import numpy as np
from sympy import *
import matplotlib.pyplot as plt


x = np.arange(1, 5000, 1)
#x = symbols('x') #求导时使用
y = (1 + ( x / 1000 ) ** 2)
z = 2 * ( 1 + ( (3000 - x) / 1000 )** 2)
m = x * y + (3000 - x)*z

####增量分配
N = 5 #迭代次数
assign = 3000 #分配流量
x_a = 1
x_b = 2
flow_a = 0
flow_b = 0
for i in range(N):
    if x_a <= x_b:
        flow_a += assign / N
        x_a = (1 + ( flow_a / 1000 ) ** 2)
        print(flow_a)
        print('x_a = {}'.format(x_a))
    else:
        flow_b += assign / N
        x_b = 2 * ( 1 + ( flow_b / 1000 )** 2)
        print(flow_b)
        print('x_b = {}'.format(x_b))

print(x_a,x_b)
