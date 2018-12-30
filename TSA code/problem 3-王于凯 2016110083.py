#----------------------------------------------------
####code for the problem 3 in TSA final tset 
#### name:王于凯 student ID:2016110083
#----------------------------------------------------
import numpy as np


x = np.arange(1, 5000, 1)
#x = symbols('x') #求导时使用
y = (1 + ( x / 1000 ) ** 2)
z = 2 * ( 1 + ( (3000 - x) / 1000 )** 2)
m = x * y + (3000 - x)*z

#diffm = diff(m, x) #求m对x的导数
#求导结果
#3*x**2/1000000 + (-x + 3000)*(x/250000 - 3/250) - 2*(-x/1000 + 3)**2 - 1

####求交点
crossover = 10000
for i in range(len(x)):
    distance = (y[i] - z[i])**2
    if distance <= crossover:
        crossover = distance
        x_point =i + 1
        y1_point = y[i]
        y2_point = z[i]

print("In UE condision, the answer are x_1 = {} and x_2 = {}".format(x_point, 3000 - x_point))


####求导为零
dm = 3*x**2/1000000 + (-x + 3000)*(x/250000 - 3/250) - 2*(-x/1000 + 3)**2 - 1
crossover = 10000
for i in range(len(x)):
    distance = (dm[i] - 0)**2
    if distance <= crossover:
        crossover = distance
        x_point = i + 1
        y_point = dm[i]

print("In SO condision, the answer are x_1 = {} and x_2 = {}".format(x_point, 3000 - x_point))
