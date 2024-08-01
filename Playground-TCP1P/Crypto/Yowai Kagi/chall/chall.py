from Crypto.Util.number import *
from secret import flag

def source(flag):
    e = 65537
    n = getStrongPrime(1024)
    m = bytes_to_long(flag)
    return [e, n, m]

def enc(source):
    a, b, c = source
    if(pow(c, a) > b):
        cp = pow(c, a, b)
        cp = long_to_bytes(cp)
        return [cp, b]

def write(data):
    file = open("output.txt", "w")
    file.write(str(data))
    file.close

sourceProc = source(flag)
encProc = enc(sourceProc)
write(encProc)