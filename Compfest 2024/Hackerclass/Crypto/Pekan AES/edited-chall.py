from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    print(pad(plaintext, 16))
    return cipher.encrypt(pad(plaintext, 16))

def decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), 16)

def menu():
    print("1. Encrypt Message")
    print("2. Get Flag")
    print("3. Exit")
    choice = int(input(">> "))
    return choice

#key = os.urandom(16)
key = b"L\xe1\xd9^u'\x08MUN0\x0e\xc9v\x11;"
print(key)

while True:
    choice = menu()
    if choice == 1:
        plaintext = input("Message: ")
        print(b'COMPFEST\x0016')
#        if 'COMPFEST16' in plaintext:
#            print("Nope.")
#            continue
        print("Encrypted Message (hex):", encrypt(key, plaintext.encode()).hex())
    elif choice == 2:
        ciphertext = input("Encrypted Message (hex): ")
        try:
            plaintext = decrypt(key, bytes.fromhex(ciphertext)).decode()
            print(plaintext)
            print(type(plaintext))
            if 'COMPFEST16' in plaintext:
                print(open('flag.txt').read())
        except:
            print("Invalid ciphertext.")
    elif choice == 3:
        break
