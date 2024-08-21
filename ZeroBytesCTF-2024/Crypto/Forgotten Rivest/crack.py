from base64 import b64encode, b64decode

ciphertext = open("pesan.txt", "r").readlines()

ciphertext = [ciphertext[x][:-1] for x in range(len(ciphertext))]

cipher = [b64decode(x) for x in ciphertext]

v7 = [
        "Sometimes, what you have been tirelessly searching for, ",
        "that elusive and significant thing, is right in front of",
        " you. It might be something important that holds the key",
        "                                                        ",
        "                                                        ",
        "                                                        "
    ]

key = []
#raw[0] ^ ord('S')
#Crack Key
for i in range(len(v7[0])):
    tmp = cipher[0][i] ^ ord(v7[0][i])
    key.append(tmp)

#Decrypt
for enc in cipher:
    tmp = ''
    for x in range(len(enc)):
        tmp += chr(enc[x] ^ key[x])
    print(tmp)