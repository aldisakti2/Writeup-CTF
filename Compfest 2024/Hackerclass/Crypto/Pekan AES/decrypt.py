from pwn import *
import string

REMOTE_HOST = "challenges.ctf.compfest.id"
REMOTE_PORT = 20015
r = remote(REMOTE_HOST, REMOTE_PORT)

def encrypt(msg):
    r.recvuntil(">> ")
    r.sendline("1")
    r.recvuntil("Message: ")
    r.sendline(msg)
    ciphertext_line = r.recvline().decode().strip()  # Get the ciphertext line
    return ciphertext_line.split(": ")[1]  # Extract ciphertext value

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

if __name__ == "__main__":
