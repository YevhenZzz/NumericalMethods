import math

from numpy import arange
import matplotlib.pyplot as plt

Umax = 100
f = 50
R1 = 5
R2 = 4
R3 = 7
R4 = 2
L1 = 0.01
L2 = 0.02
L3 = 0.015
C1 = 300 * math.pow(10, -6)
C2 = 150 * math.pow(10, -6)
C3 = 200 * math.pow(10, -6)
T = 0.2
h = 0.0001
Y = [0] * 2
X = [0] * 2


def func1(x0, x1):
    return (U1 - x0 + x1 * R2) / (R1 + R2) / C1


def func2(x0, x1):
    return (R2 * (U1 - x0 - x1 * R1) / (R1 + R2) - x1 * (R3 + R4)) / L1


if __name__ == '__main__':
    for t in arange(0, (T - h / 2), h):
        U1 = Umax * math.sin(2 * math.pi * f * t)

        X[0] = X[0] + h * func1(X[0], X[1])
        X[1] = X[1] + h * func2(X[0], X[1])

        U2 = X[1] * R4
        print(str(U2) + '\t' + str(t))
        plt.plot(t + h, U2, 'ro')

    plt.xlabel(r'$t$')
    plt.ylabel(r'$U2$')
    plt.grid(True)
    plt.show()