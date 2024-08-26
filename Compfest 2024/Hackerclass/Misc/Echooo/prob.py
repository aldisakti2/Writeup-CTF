#!/usr/bin/env python3
import os
import sys

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)

while(1):
    x = input('Gimme your input: ')
    y = ''
    for c in x:
        if (not c.isalnum()):
            y += c

    print('Your input:', y)
    os.system('echo ' + y)
