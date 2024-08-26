import pyshark

f = pyshark.FileCapture('traffic.pcapng', display_filter="ip.flags.rb == 1")

flag = b''

for p in f:
    flag += bytes.fromhex(str(p['tcp'].payload))

print(flag.decode())

#print(result)


