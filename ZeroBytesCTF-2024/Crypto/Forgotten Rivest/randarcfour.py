import time
import random
import base64

def rc4(key, key_length, data, data_length):
    v6 = list(range(256))
    v10 = 0
    
    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        v10 = (v6[i] + v10 + key[i % key_length]) % 256
        v6[i], v6[v10] = v6[v10], v6[i]
    
    # Pseudo-Random Generation Algorithm (PRGA)
    v10 = 0
    i = 0
    output = bytearray()
    other = []
    
    for j in range(data_length):
        i = (i + 1) % 256
        v10 = (v10 + v6[i]) % 256
        v6[i], v6[v10] = v6[v10], v6[i]
        other.append(v6[(v6[i] + v6[v10]) % 256])
        other.append(data[j])
        output.append(v6[(v6[i] + v6[v10]) % 256] ^ data[j])

    return output, other

# Main function equivalent
def main():
    # Seed the random number generator with current time
    random.seed(int(time.time()))

    # Generate a 32-byte random key
    v8 = bytearray(random.getrandbits(8) for _ in range(32))
    print(v8)
    # Text data
    v7 = [
        "Sometimes, what you have been tirelessly searching for, ",
        "that elusive and significant thing, is right in front of",
        " you. It might be something important that holds the key",
        "                                                        ",
        "                                                        ",
        "                                                        "
    ]
    
    # Process each line
    for s in v7:
        s_bytes = bytearray(s, 'utf-8')
        v6, key = rc4(v8, len(v8), s_bytes, len(s_bytes))
        v5 = base64.b64encode(v6).decode('utf-8')
        print(v5, key)

# Execute the main function
if __name__ == "__main__":
    main()
