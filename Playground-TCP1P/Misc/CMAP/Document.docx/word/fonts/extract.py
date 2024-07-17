#!/usr/bin/env python3

import os
import sys

fn_in = sys.argv[1]
fn_out = os.path.splitext(sys.argv[1])[0] + '.ttf'
print(fn_out)
# Parse
key = os.path.splitext(os.path.basename(fn_in))[0].replace('-', '')
# Convert to Int reversed
key_int = [int(key[i-2:i], 16) for i in range(32, 0, -2)]

with open(fn_in, 'rb') as fh_in, open(fn_out, 'wb') as fh_out:
	cont = fh_in.read()
	fh_out.write(bytes(b ^ key_int[i % len(key_int)] for i, b in enumerate(cont[:32])))
	fh_out.write(cont[32:])
