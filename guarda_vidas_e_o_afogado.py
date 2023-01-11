import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, root_scalar

def tempo(xs, xt, ys, yw, vs, vw):
    ts = np.sqrt(xs**2 + ys**2) / vs
    tw = np.sqrt((xt - xs)**2 + yw**2) / vw
    return ts + tw

def dtdxs(xs, xt, ys, yw, vs, vw):
    dts = xs / (vs * np.sqrt(xs**2 + ys**2))
    dtw = (xs - xt) / (vw * np.sqrt((xt - xs)**2 + yw**2))
    return dts + dtw

if __name__ == '__main__':
    xt = 100.0
    ys = 25.0
    yw = 150.0
    vs = 3.0
    vw = 0.5

# Gráfico + força bruta
    xs = np.linspace(0.0, xt, 1000)
    t = tempo(xs, xt, ys, yw, vs, vw)
    plt.plot(xs, t, '-ob')
    plt.show()
    idx = np.argmin(t)
    tmin = t[idx]
    xsmin = xs[idx]
    err_t = t[idx-1] - tmin 
    print('*** Força bruta ***')
    print(f'O tempo mínimo é {tmin:.1f} segundos na posição xs = {xsmin:.1f} metros.')
    print(f'A estimativa do erro no tempo mínimo é {err_t:.1e} segundos.')

# minimize_scalar da scipy
    m = minimize_scalar(tempo, bracket=(0,xt), args=(xt, ys, yw, vs, vw), method='brent', tol=err_t)
    print('*** Minimize_scalar ***')
    print(f'O tempo mínimo é {m.fun:.1f} segundos na posição xs = {m.x:.1f} metros.')
    print(f'Calculou a função {m.nfev:d} vezes.')

# root_scalar
    r = root_scalar(dtdxs, args=(xt, ys, yw, vs, vw), method='brentq', bracket=(0,xt), xtol=err_t, rtol=err_t)
    print('*** Root_scalar ***')
    print(f'O tempo mínimo é {m.fun:.1f} segundos na posição xs = {r.root:.1f} metros.')
    print(f'Calculou a função {r.function_calls:d} vezes.')






