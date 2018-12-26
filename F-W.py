import numpy as np

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

for i in range(100):
    path1 = (1 + ( xn[0] / 1000 ) ** 2)
    path2 = 2 * ( 1 + ( xn[1] / 1000 )** 2)

    if path1 < path2:
        yn[0] = assign
    else:
        yn[1] = assign


    #x = symbols('x')
    x_a = np.arange(0, 3000, 0.001)
    inte1 = []
    #inte = sympy.integrate((1 + ( x / 1000 ) ** 2),(x))
    #x**3/3000000 + x
    inte2 = []
    #inte = sympy.integrate(((2 * ( 1 + ( (3000 - x) / 1000 )** 2), x)))
    #x**3/1500000 + 2*x

    for i in x_a:
        i = i
        combine1 = (1 - i) * xn[0] + i * yn[0]
        combine2 = (1 - i) * xn[1] + i * yn[1]
        inte1.append(combine1**3/3000000 + i)
        inte2.append(combine2**3/1500000 + 2*combine2)

    crossover = 10000000000
    for i in range(len(inte2)):
        distance = (inte1[i] + inte2[i])
        if distance <= crossover:
            crossover = distance
            x_point = (i+1)*0.001
            y_point = distance
    print(x_point)
    xn[0] = (1 - x_point)*xn[0] + x_point*yn[0]
    xn[1] = (1 - x_point)*xn[1] + x_point*yn[1]
    print(xn)



'''''
while True:
    if tf1 < tf2:
        xn[0] = assign
    else:
        tf2 = 2*(1 + ( assign / 1000 ) ** 2)
    #inte = sympy.integrate((1 + ( x / 1000 ) ** 2),(x))
    #x**3/3000000 + x
    x_a = np.arange(0, 3000, 0.01)
    for i in x_a:
        combine = (1-i)*tf1 + i*tf2
        z = combine**3/3000000 + combine
'''''
