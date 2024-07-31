from scapy.all import *
from typing import Dict

print('[+] Start ....')
pcap = rdpcap('../help/desktop.pcap')
data: Dict[int, Dict[int, bytes]] = {}
print('[+] Try parsing the pcap')
for pkt in pcap:
    try:
        if pkt[ICMP].type == 8: #response
            tmp: Dict[int, bytes] = {}
            c = pkt[ICMP].seq
            c = c - 1
            j = c // 256
            k = c >> j if j > 0 else c
            rdm = sum([ord(i) for i in str(pkt.time)[0:8]]) >> 3
            rdmz = rdm ^ k
            id = pkt[ICMP].id
            y = pkt.load
            tmp[c] = bytes(a[0] ^ rdmz for a in zip(y))
            try:
                data[id].update(tmp)
            except:
                data[id] = tmp
    except:
        continue

print('[+] Reshuffle the packet')
result = dict()
for key, val in data.items():
    sorted_key = list(val.keys())
    sorted_key.sort()
    sorted_dict = {i: val[i] for i in sorted_key}
    for key2, val2 in sorted_dict.items():
        try:
            result[key] += val2
        except:
            result[key] = val2

print('[+] Rebuild the file')
for key, val in result.items():
    out = open(f'res/{key}.zip','wb')
    out.write(val)
