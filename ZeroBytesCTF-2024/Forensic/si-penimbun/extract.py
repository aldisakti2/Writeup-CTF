#import numpy as np
from d2b import d2b

data = open('image.png', 'rb').read()

part_data = [data[0+i:i+28] for i in range(0, len(data), 29)]

real_data = []

position = 0

while position != 27:
    for data in part_data:
        real_data.append(d2b(data[position]))
    with open(f'part{position}.png', 'wb') as f:
        for i in real_data:
            f.write(i)
        f.close()
    real_data = []
    position += 1
    print(f'File part{position}.png is generated...')
