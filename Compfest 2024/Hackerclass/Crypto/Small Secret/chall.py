from Crypto.Util.number import *
from Crypto.Util.Padding import pad

p = getPrime(256)
q = getPrime(256)
n = p * q

while True:
    d = getPrime(128)
    if GCD(d, (p - 1) * (q - 1)) == 1:
        e = inverse(d, (p - 1) * (q - 1))
        break

flag = b"COMPFEST16{REDACTED}"

m = bytes_to_long(pad(flag, n.bit_length() // 8))
c = pow(m, e, n)
print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")
