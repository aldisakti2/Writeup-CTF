#!/usr/bin/env python3

import os
import sys


fontTableMap = {
    "rId1": "3699E84F-E21F-425D-BBD7-47A4A7E8CD7A",
    "rId2": "12BBC437-D46E-4856-9231-58A183AC33A5",
    "rId3": "12222F5F-D1ED-4AE3-BE82-7E19C7DBFFC4",
    "rId4": "259EBEE4-DA14-4B3B-B7F6-C33D1577B046",
    "rId5": "C104906A-E809-4DF0-AFFA-6FC60E11874A",
    "rId6": "D7C3CD72-40BA-4B25-BC47-41D4822C7E7D",
    "rId7": "B6AF6720-2288-49E8-A23C-AB06A37CBFFE"
}

xmlTableMap = {
    "rId3": "font3.odttf",
    "rId7": "font7.odttf",
    "rId2": "font2.odttf",
    "rId1": "font1.odttf",
    "rId6": "font6.odttf",
    "rId5": "font5.odttf",
    "rId4": "font4.odttf"
}

def mapFont(font, xmlTable, fontTable):
    key = ""
    for x in xmlTable:
        if font == xmlTable[x]:
            key = x
            break

    return fontTable[key]


fn_in = sys.argv[1]
fn_out = os.path.splitext(sys.argv[1])[0] + '.ttf'
print(fn_out)
# Parse

#key = os.path.splitext(os.path.basename(fn_in))[0].replace('-', '') #Versi Original
key = mapFont(fn_in, xmlTableMap, fontTableMap).replace('-', '') #Versi Custom

# Convert to Int reversed
key_int = [int(key[i-2:i], 16) for i in range(32, 0, -2)]

with open(fn_in, 'rb') as fh_in, open(fn_out, 'wb') as fh_out:
	cont = fh_in.read()
	fh_out.write(bytes(b ^ key_int[i % len(key_int)] for i, b in enumerate(cont[:32])))
	fh_out.write(cont[32:])
