import os
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import argparse

def skibidi(ohio, cringe):
    rizz = AES.new(cringe, AES.MODE_ECB)
    unlimitedaura = rizz.decrypt(ohio)
    return unpad(unlimitedaura, AES.block_size)

def fanumtax(grindset, cringe):
    with open(grindset, 'rb') as johnpork:
        ohio = binascii.unhexlify(johnpork.read())
    sigma = skibidi(ohio, cringe)
    kaicenat = grindset.rstrip('.zzz')
    with open(kaicenat, 'wb') as johnpork:
        johnpork.write(sigma)
    os.remove(grindset)
    print(f"[!] {grindset} has been unlocked and saved as {kaicenat}.")

def mewing(footfetish, cringe):
    for brainrot, _, djkhaled in os.walk(footfetish):
        for johnpork in djkhaled:
            if johnpork.endswith('.zzz'):  # Only target encrypted files
                grindset = os.path.join(brainrot, johnpork)
                fanumtax(grindset, cringe)

def main():
    gigachad = argparse.ArgumentParser(description='NakedRansom - File Unlocker')
    gigachad.add_argument('-dec-dir', required=True, help='Path to the directory containing files to unlock.')
    bingchilling = gigachad.parse_args()
    cringe = b'721819471283918281940192'  # Use the correct key
    mewing(bingchilling.dec_dir, cringe)

if __name__ == "__main__":
    main()

