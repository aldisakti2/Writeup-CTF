import pyshark

def extract_packet_info(pcap_file):
    cap = pyshark.FileCapture(pcap_file)
    packet_info_list = []

    for packet in cap:
        try:
            if packet.transport_layer == 'TCP':
                src_port = int(packet.tcp.srcport)
                dst_port = int(packet.tcp.dstport)
                flags = packet.tcp.flags
#                analysis = packet.frame_info.number
                packet_info_list.append({'src_port': src_port, 'dst_port': dst_port, 'flags': flags})
        except AttributeError:
            # Ignore packets that don't have the necessary layers/attributes
            continue

    cap.close()
    return packet_info_list

result = ""

if __name__ == "__main__":
    pcap_file = 'log.pcap'
    packet_info = extract_packet_info(pcap_file)
    for i in range(1,len(packet_info)):
        tmp = packet_info[i-1]['dst_port']
        flag = packet_info[i-1]['flags']
        if tmp != packet_info[i]['src_port'] and flag == '0x0002':
            result += chr(int(tmp))
    print(result)
#'0x0002'
#'src_port': 67, 'dst_port': 20
