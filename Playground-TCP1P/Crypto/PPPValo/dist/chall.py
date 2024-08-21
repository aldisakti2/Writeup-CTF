from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from libnum import s2n
flag = open("./src/flag.txt", "rb").read()
#print(flag)
flag = b"TCP1P{PERCOBAAN}"
assert(flag.startswith(b"TCP1P{"))
flag = flag.replace(b'TCP1P{', b'')
assert(flag.endswith(b"}"))
flag = flag.replace(b'}', b'')

key = RSA.generate(1024)
cipher = PKCS1_OAEP.new(key)
ct = cipher.encrypt(flag)
with open(r'./src/flag.enc', 'w+') as f:
    f.write(f"{key.n=}\n")
    f.write(f"{key.p=}\n")
    f.write(f"{key.q=}\n")
    f.write(f"{key.invp=}\n")
    f.write(f"{key.invq =}\n")
    f.write(f"{ct=}\n")

