from Crypto.Util.number import *

flag1 = b"TCP1P{xxxxxxxxxxxxxxxxxxxxxx"
flag2 = b"xxxxxxxxxxxxxxxxxxxxxxxxxxx}"

m1 = bytes_to_long(flag1)
m2 = bytes_to_long(flag2)

# Euclidean algorithm
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Extended euclidean algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

# First part (GCD)
c1 = m1**2 + 23
c2 = m1*getPrime(216)

# Second part (EGCD)
x = egcd(c1,c2)[1]
y = egcd(c1,c2)[2]
c3 = m2*x*y

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c3 = {c3}")
