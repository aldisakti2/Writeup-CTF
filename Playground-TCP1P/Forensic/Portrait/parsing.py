import pyshark

KEY_CODES = {
    0x04: ['a', 'A'],
    0x05: ['b', 'B'],
    0x06: ['c', 'C'],
    0x07: ['d', 'D'],
    0x08: ['e', 'E'],
    0x09: ['f', 'F'],
    0x0A: ['g', 'G'],
    0x0B: ['h', 'H'],
    0x0C: ['i', 'I'],
    0x0D: ['j', 'J'],
    0x0E: ['k', 'K'],
    0x0F: ['l', 'L'],
    0x10: ['m', 'M'],
    0x11: ['n', 'N'],
    0x12: ['o', 'O'],
    0x13: ['p', 'P'],
    0x14: ['q', 'Q'],
    0x15: ['r', 'R'],
    0x16: ['s', 'S'],
    0x17: ['t', 'T'],
    0x18: ['u', 'U'],
    0x19: ['v', 'V'],
    0x1A: ['w', 'W'],
    0x1B: ['x', 'X'],
    0x1C: ['y', 'Y'],
    0x1D: ['z', 'Z'],
    0x1E: ['1', '!'],
    0x1F: ['2', '@'],
    0x20: ['3', '#'],
    0x21: ['4', '$'],
    0x22: ['5', '%'],
    0x23: ['6', '^'],
    0x24: ['7', '&'],
    0x25: ['8', '*'],
    0x26: ['9', '('],
    0x27: ['0', ')'],
    0x28: ['\n', '\n'],
    0x29: ['[ESC]', '[ESC]'],
    0x2a: ['[BACKSPACE]', '[BACKSPACE]'],
    0x2C: [' ', ' '],
    0x2D: ['-', '_'],
    0x2E: ['=', '+'],
    0x2F: ['[', '{'],
    0x30: [']', '}'],
    0x31: ['\\', '|'],
    0x32: ['#', '~'],
    0x33: [';', ':'],
    0x34: ['\'', '"'],
    0x36: [',', '<'],
    0x37: ['.', '>'],
    0x38: ['/', '?'],
    0x39: ['[CAPSLOCK]', '[CAPSLOCK]'],
    0x2b: ['\t', '\t'],
    0x4f: ['\u2192', '\u2192'],
    0x50: ['\u2190', '\u2190'],
    0x51: ['\u2193', '\u2193'],
    0x52: ['\u2191', '\u2191']
}

def filter(packet):
    if "a1:01:00:00:00:00:00:00:00:00" in packet or "a1:01:02:00:00:00:00:00:00:00" in packet or "a1:01:20:00:00:00:00:00:00:00" in packet:
        return False
    return True

f = pyshark.FileCapture('portrait.pcapng', display_filter="btl2cap")
output = ''
result = []

for p in f:
    packet = p['btl2cap'].payload
    if filter(packet):
        data = packet.split(":")
        try:
            shift = int(data[2], 16)  # 0x2 is left shift 0x20 is right shift
            key = int(data[4], 16)

            if shift == 2 or shift == 32:
                shift = 1

            if KEY_CODES[key][shift] == '\u2191':
                output += KEY_CODES[key][shift]
                print(output)
                result.append(output)
                output = ''
            elif KEY_CODES[key][shift] == '\u2193':
                output += KEY_CODES[key][shift]
                print(output)
                result.append(output)
                output = ''
            elif KEY_CODES[key][shift] == '\n':
                result.append(output)
                result.append("\n")
                print(output)
                print("")
                output = ''
            else:
                output += KEY_CODES[key][shift]
        except (IndexError, ValueError, KeyError) as e:
            print(f"Skipping invalid data line: {data}")
            continue


print(result)
