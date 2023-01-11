import math as mt
import sys

v0 = float(input('Entre com a velocidade inicial (m/s): '))
ang = float(input('Entre com o ângulo de lançamento (graus): '))
d1 = 6.0
d2 = 3.6
g = 9.8
ang = mt.radians(ang)

if mt.tan(ang) < d2/d1 or ang > mt.pi/2:
    ang_min = mt.degrees(mt.atan(d2/d1))
    sys.exit(f'O ângulo de lançamento deve ser entre {ang_min:.1f} e 90 graus.')

p = 2 * v0**2 * mt.cos(ang)**2 / g
xt = p * (mt.tan(ang) - d2/d1)

if xt < d1:
    print(f'A bola caiu na rampa: x = {xt:.2f} m | y = {d2*xt/d1:.2f} m.')
else:
    a = 1  / p
    b = -mt.tan(ang)
    c = d2
    xt = (-b + mt.sqrt(b**2 - 4 * a * c)) / (2 * a)
    print(f'A bola caiu no platô: x = {xt:.2f} m | y = {d2:.2f} m.')
