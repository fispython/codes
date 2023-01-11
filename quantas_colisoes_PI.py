def colisao (v1i, v2i, m1, m2):
    m_pos = m1 + m2
    m_neg = m1 - m2

    v1f = m_neg * v1i / m_pos + 2 * m2 * v2i / m_pos
    v2f = 2 * m1 * v1i / m_pos - m_neg * v2i / m_pos
    return v1f, v2f

ncols = 0
m1 = 1.e12
m2 = 1.
v1 = -1.
v2 = 0.

v1, v2 = colisao (v1, v2, m1, m2)
ncols += 1

while True:
    if v2  < 0: # vai bater na parede
        v2 = -v2
        ncols += 1

    if v2 > v1: # vai bater na particula 1
        v1, v2 = colisao (v1, v2, m1, m2)
        ncols += 1
    else: # vai nada
        break

print('O número de colisões foi: ', ncols)

