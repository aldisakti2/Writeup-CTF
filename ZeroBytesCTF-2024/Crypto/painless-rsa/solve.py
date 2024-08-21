from sympy import factorint, mod_inverse
from Crypto.Util.number import long_to_bytes

n = 7966195708392053893
factors = factorint(n)

p = list(factors.keys())[0]
q = list(factors.keys())[1]
phi_n = (p - 1) * (q - 1)
e = 65537

d = mod_inverse(e, phi_n)

def decrypt_rsa(c, d, n):
    return pow(c, d, n)

flag_values = [
    3603559738529170956,
    6962242565162788762,
    1128158985794307978,
    3555769816747854624,
    3840731448945647355,
    4790155366113405289,
    6685007257211276224,
    6683171830083696223,
    303480981645266723,
    7136855732243656947,
    4724274163147438738,
    3840302861364940231,
    6472219297830075118,
    478945534552876439,
    1757721247936442303
]

flag = ""

for value in flag_values:
    decrypted_value = decrypt_rsa(value, d, n)
    flag += long_to_bytes(decrypted_value).decode()

print(flag)

