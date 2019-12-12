import matplotlib.pyplot as plot

a = 0.09
T = 2 * a
t_integ = 5 * T
h = T / 400

C1 = 44 / 1000
C2 = 16 / 1000

L_MAX = 4.2
L_MIN = 0.42

i_MAX = 2
i_MIN = 1

R1 = 7.1
R2 = 9.2
R3 = 37
R4 = 70

Uc1 = 0
Uc2 = 0
i2 = 0

t = 0

X1_old = 0
X2_old = 0
X3_old = 0

t_values = []
U2_values = []
U1_values = []
Uc1_values = []
i2_values = []
Uc2_values = []


def U1_v(t):
    k = 0
    while (t - k * T) > T:
        k += 1
    temps = t - k * T
    temps = round(temps, 4)
    if 0 < temps <= a:
        return 10
    elif a < temps <= 2 * a:
        return 0
    else:
        return 0


def L2_v(i):
    if i <= i_MIN:
        return L_MAX
    elif i >= i_MAX:
        return L_MIN
    elif i_MIN < i < i_MAX:
        b1 = (2 * (i - i_MIN) + h) * (i_MAX - i) * (i_MAX - i)
        b2 = (2 * (i_MAX - i) + h) * (i - i_MIN) * (i - i_MIN)
        b3 = (i - i_MIN) * (i_MAX - i) * (i_MAX - i)
        b4 = (i - i_MIN) * (i - i_MIN) * (i - i_MIN)

        m1 = 0
        m2 = 0

        return (b1 * L_MAX + b2 * L_MIN) / h / h / h + (b3 * m1 + b4 * m2) / h / h


def F1(Uc1, i2, Uc2, U1):
    return (i2 + (U1 - Uc1) / R3 - Uc1 / R1) / C1


def F2(Uc1, i2, Uc2, U1):
    return (U1 - Uc1 - Uc2 - i2 * (R2 + R4)) / L2_v(i2)


def F3(Uc1, i2, Uc2, U1):
    return i2 / C2


def U2(i2, Uc2):
    return i2 * R4 + Uc2


while t < t_integ*5:
    t = round(t, 4)
    t_values.append(t)
    U1 = U1_v(t)
    U1_values.append(U1)
    U2_values.append(U2(X2_old, X3_old))
    Uc1_values.append(X1_old)
    i2_values.append(X2_old)
    Uc2_values.append(X3_old)

    K1 = h * F1(X1_old, X2_old, X3_old, U1)
    K2 = h * F1(X1_old + K1 / 3, X2_old + h / 3, X3_old + h / 3, U1)
    K3 = h * F1(X1_old - K1 / 3 + K2, X2_old + 2 * h / 3, X3_old + 2 * h / 3, U1)
    K4 = h * F1(X1_old + K1 - K2 + K3, X2_old + h, X3_old + h, U1)
    X1 = X1_old + (K1 + 3 * (K2 + K3) + K4) / 8

    K1 = h * F2(X1_old, X2_old, X3_old, U1)
    K2 = h * F2(X1_old + h / 3, X2_old + K1 / 3, X3_old + h / 3, U1)
    K3 = h * F2(X1_old + 2 * h / 3, X2_old - K1 / 3 + K2, X3_old + 2 * h / 3, U1)
    K4 = h * F2(X1_old + h, X2_old + K1 - K2 + K3, X3_old + h, U1)
    X2 = X2_old + (K1 + 3 * (K2 + K3) + K4) / 8

    K1 = h * F3(X1_old, X2_old, X3_old, U1)
    K2 = h * F3(X1_old + h / 3, X2_old + h / 3, X3_old + K1 / 3, U1)
    K3 = h * F3(X1_old + 2 * h / 3, X2_old + 2 * h / 3, X3_old - K1 / 3 + K2, U1)
    K4 = h * F3(X1_old + h, X2_old + h, X3_old + K1 - K2 + K3, U1)
    X3 = X3_old + (K1 + 3 * (K2 + K3) + K4) / 8

    X1_old = X1
    X2_old = X2
    X3_old = X3

    t += h

plot.plot(t_values, U2_values)
plot.plot(t_values, U1_values)
plot.plot(t_values, Uc1_values)
plot.plot(t_values, i2_values)
plot.plot(t_values, Uc2_values)
plot.show()