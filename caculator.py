import numpy as np
#from sympy import *
#import matplotlib.pyplot as plt


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


####求交点
crossover = 10000
for i in range(len(x)):
    distance = (y[i] - z[i])**2
    if distance <= crossover:
        crossover = distance
        x_point = i + 1 
        y1_point = y[i]
        y2_point = z[i]

print(x_point, y1_point)

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
        

