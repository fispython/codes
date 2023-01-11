import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

def alcance(theta, v0, g):
    return v0**2 * np.sin(2 * theta) / g

def arg_int(x, theta, v0, g):
    dydx = np.tan(theta) - g * x / (v0 * np.cos(theta))**2
    return np.sqrt(1. + dydx**2)

def arg_minimize(theta, v0, g):
    A = alcance(theta, v0, g)
    return -quad(arg_int, 0, A, args=(theta, v0, g), epsabs=0, epsrel=1.e-12)[0]


if __name__ == "__main__":
    v0 = 10.0
    g = 9.8
    theta = np.linspace(0.0, np.pi/2, 1000)
    d_list = []
    A_list = []

    for t in theta:
        A = alcance(t, v0, g)
        dist = quad(arg_int, 0, A, args=(t, v0, g), epsabs=0, epsrel=1.e-12)[0]
        d_list.append(dist)
        A_list.append(A)

    plt.plot(np.degrees(theta), A_list, '-r', label='Alcance')
    plt.plot(np.degrees(theta), d_list, '-b', label='Comprimento')
    plt.xlabel('ângulo de lançamento (graus)')
    plt.legend()
    plt.show()

    m = minimize_scalar(arg_minimize, bracket=[0, np.pi/2], args=(v0, g), method='brent', tol=1.e-12)
    print(np.degrees(m.x))







