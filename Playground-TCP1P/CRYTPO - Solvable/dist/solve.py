from sage.all import *

N = 0x11b4c225f4dc385553faef71fd12d7a7d3731eebb47d01df2bd9c06cc95d67d933a3867dc3ef17547ae5a969dbc985489a3e835ddb0f8e1eb82b2cb84a5b168f74a808a0b7accbc1513cd416a5e8a4055a2823e192bdbe5da3583b11b0a1697a5a47
e = 65537

with open("output.txt", "r") as f:
    n, u, c = [int(i.split(" = ")[1]) for i in f.readlines()]

P = PolynomialRing(Zmod(N),'x', implementation='NTL')
x = P.gen()
f = (x**3 + x + 1 - u * x**2)
for root in f.roots():
    dqr = int((root[0]).log(e))
    if dqr.bit_length() <= 512:
        break

R = PolynomialRing(Zmod(n), 'y', implementation='NTL')
y = R.gen()
kbits = 1024 - dqr.bit_length()
f = (y * 2 ** dqr.bit_length() + dqr).monic()
s = f.small_roots(X=2 ** kbits, beta=0.3, epsilon=0.01)[0]
qr = s * (1 << dqr.bit_length()) + dqr

p = int(n) // int(qr)
msg = pow(c, inverse_mod(e, p-1), p)

print(bytes.fromhex(hex(msg)[2:]))
