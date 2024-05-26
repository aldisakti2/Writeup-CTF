from hashlib import md5

data = open('../chall/decryption_server.log', 'r').readlines()

digests = []
tmp = []
for line in data:
    if "Partial" in line:
        tmp.append(line.split()[-1])
    elif "Message fully" in line:
        digests.append(tmp)
        tmp = []

data_arr = []
tmp_arr = bytearray()

for r in range(len(digests)):
    if len(data_arr) == 0 and len(tmp_arr) != 0:
        data_arr.append(tmp_arr)
        tmp_arr = bytearray()
    if len(data_arr) != 0:
        data_arr.append(tmp_arr)
        tmp_arr = bytearray()
    for c in range(len(digests[r])):
        for i in range(128):
            tmp_arr.append(i)
            tmp = md5(tmp_arr).hexdigest()
            if tmp == digests[r][c]:
                break
            else:
                tmp_arr.pop()

for i in data_arr:
    print(i.decode())


