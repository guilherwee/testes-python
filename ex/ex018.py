import math
an = float(input('digite o angulo q deseja?'))
r = math.radians(an)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print(
    f'se o angulo for {an} \n o seno sera {s:.3f} \n o coseno sera{c:.3f} \n e a trangente sera {t:.3f}')
