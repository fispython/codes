import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def terra_sol(t, y):
    f = np.empty_like(y)
    r3 = (y[0]**2 + y[2]**2)**1.5

    f[0] = y[1]
    f[1] = -y[0] / r3
    f[2] = y[3]
    f[3] = -y[2] / r3

    return f

if __name__ == '__main__':

    t = np.linspace(0, 1000, 10000)
    ts = (t.min(), t.max())
    y0 = [1., 0., 0., 0.99*np.sqrt(2)]
    s = solve_ivp(terra_sol, t_span=ts, y0=y0, method='DOP853', t_eval=t, atol=1.e-50, rtol=1.e-12)

    energia = 0.5 * (s.y[1]**2 + s.y[3]**2) - 1 / np.sqrt(s.y[0]**2 + s.y[2]**2) 
    ell = s.y[0] * s.y[3] - s.y[2] * s.y[1]

    plt.plot(s.y[0], s.y[2], '-b')
    plt.show()
    plt.plot(s.t, energia, '-b')
    plt.axhline(0.5 * s.y[3][0]**2 - 1, c='r')
    plt.show()
    plt.plot(s.t, ell, '-b')
    plt.axhline(s.y[3][0], c='r')
    plt.show()
