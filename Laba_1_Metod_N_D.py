import numpy as np
from random import uniform

MIN, MAX = 0, 20
a0, a1, a2, a3 = 2, 1, 3, 3

x = np.empty((8, 3), dtype=float)
y = np.empty(8)
x0 = np.empty(3)
dx = np.empty(3)
xNormal = np.empty((8, 3), dtype=float)

for i in range(8):
    for j in range(3):
        x[i, j] = uniform(MIN, MAX)

for i in range(8):
    y[i] = a0 + a1 * x[i, 0] + a2 * x[i, 1] + a3 * x[i, 2]

for i in range(3):
    x0[i] = (x[:, i].max() + x[:, i].min()) / 2
    dx[i] = x[:, i].max() - x0[i]
y_et = a0 + a1 * x0[0] + a2 * x0[1] + a3 * x0[2]

for i in range(8):
    for j in range(3):
        xNormal[i, j] = (x[i, j] - x0[j]) / dx[j]

dy = 999999
Number = -1

for i in range(8):
    if y[i] - y_et < dy and y[i] - y_et > 0:
        dy = y[i] - y_et
        Number = i

y2 = a0 + a1 * x[Number, 0] + a2 * x[Number, 1] + a3 * x[Number, 2]

print("x:\n", x)
print("y:\n", y)
print("x0: \n", x0)
print("y_et = ", y_et)
print("xNormal: \n", xNormal.round(4))
print("Number = ", Number)
