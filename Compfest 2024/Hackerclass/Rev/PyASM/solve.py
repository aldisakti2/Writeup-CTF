from math import sqrt

x = [0] * 9

x[7] = 120 - 69
x[3] = 114
x[0] = 110
x[4] = 51

for i in range(1024):
	if i << 3 == 832:
		x[8] = i
		break

x[1] = int(sqrt(9409))
x[6] = int(693//7)
x[2] = 109
x[5] = 107

print(''.join(chr(x) for x in x[::-1]))
