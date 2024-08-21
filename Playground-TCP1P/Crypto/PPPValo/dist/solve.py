from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import inverse, GCD, long_to_bytes
import gmpy2

# Replace these with actual values from your file
n=108968789941102923575789782324105157048081583298436404233965777037328275395317447971475170222848170276248363720650211191108917184545108194739700861856535002088548988035805537888053797268684664758612721011514012937464195321586643070395256055917268428154404753024032378570647091443869315108151218791577942089217
invp=7407291125786135381861433253169371480648843772183363165710942438089125700005320653922706631492560245328549554249050934552008453971401732902171951518473109
invq =3212083205272723147020980709364704405125727104023370781697451020238629472626925494104933395667410442713964562283771868303355788208668239546450045357418477
ct=b'\x95\x1c\xfc\x9e\x81\xe6\\l\x0b4\x1a\x0e\xba\x95\xb1\x9d\xb9\xb1\xa9\xc9\x91\x98\xdb\xa8\xa6;\xb8P\x12\xcb\xf9\x1e\xf0\xab\x84\x9f \xe4\x90\x10\xb5+6Hy \xc0\x99\xdf\xea\x83\x80\xe5\xf8\x97\xbdJ2\x8a\xd0\x97\xb4\xba\xb4\x13\xcb\x93\x86E\xbe\xceK\xea3\xedL5\'\x86\xef\x92\x1d\xc4\x07m3\x00|\x02\xden\xe9\xd8om\xb2\x08\xda2"=\xa0\xbaj\x9e5=\x8f\x9cv\xa2\xb5T\xb6\xc0\xe80\xa8\x11\xbc\x95R\x0c\xf7\xd6Ai\x9d'

def recover_p_q(n, invp, invq):
    # Step 1: Find the GCD of invp and n to derive a candidate p and q
    g = GCD(invp, n)
    if g == 1:
        raise ValueError("GCD of invp and n is 1, which should not happen")

    # Step 2: Calculate p and q using modular arithmetic
    p_candidate = (invp * g - 1) % n
    q_candidate = n // p_candidate

    # Verify the correctness of p and q
    if p_candidate * q_candidate == n:
        return p_candidate, q_candidate
    else:
        raise ValueError("Failed to find valid p and q")

# Recover p and q
p, q = recover_p_q(n, invp, invq)

print(f"p: {p}")
print(f"q: {q}")

# Step 3: Reconstruct the private key
e = 65537  # Commonly used public exponent
d = inverse(e, (p - 1) * (q - 1))
private_key = RSA.construct((n, e, d, p, q))

# Step 4: Decrypt the ciphertext
cipher = PKCS1_OAEP.new(private_key)
flag = cipher.decrypt(ct)

print(flag.decode())

