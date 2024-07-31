import pyshark

f = pyshark.FileCapture('log.pcap', display_filter="tcp and tcp.flags.reset == 1 and tcp.flags.ack == 1")
output = ''

for p in f:
    packet = chr(int(p.tcp.srcport))
    output += packet
print(output)
