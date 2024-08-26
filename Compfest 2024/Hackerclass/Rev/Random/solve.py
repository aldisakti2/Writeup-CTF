import random

real =  b'!vP3\xc2\x91\xc2\x89\x11\x1f\x06C\x17_\x19t)\xc2\x929\x06li\x1d\x1f\xc2\x88*\x19E+4E\x16\x07v1S$\x1a c\x1flcr4> 3vlt\xc2\x85Yj-$0 '

flag = "COMPFEST16{" # REDACTED

def attack(flag):
    random.seed(int(flag[8:10]))
    for c in flag[:8]:
        random.seed(random.randint(1, 0xCF) + ord(c))
        #print("C: ", c)

    destroyed = ""

    for char in flag:
        offset = random.randint(1, 10)
        #print("Offset: ", offset)
        MyFriend = random.randint(1, 127)
        #print("MyFriend: ", MyFriend)
        result = (ord(char) - offset) ^ MyFriend

        if random.randint(0, 1):
            #print("HIGH")
            result += 0x16
    
        destroyed += chr(result)

    return destroyed.encode("utf-8")


for x in range(len(real)):
    for i in range(32,128):
        tmp = attack(flag+chr(i))
        if tmp == real[:14+x]:
            print(flag+chr(i))
            flag += chr(i)
