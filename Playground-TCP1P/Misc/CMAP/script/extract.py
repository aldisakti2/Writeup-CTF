map_key = {
    'zero': 0x0, #0
    'onesuperior': 0x1, #1
    'twosuperior': 0x2, #2
    'threesuperior': 0x3, #3
    'four': 0x4, #4
    'five': 0x5, #5
    'six': 0x6, #6
    'seven': 0x7, #7
    'eight': 0x8, #8
    'nine': 0x9, #9
    'afii10065': 'a', #a
    'afii10094': 'b', #b
    'afii10083': 'c', #c
    'd': 'd', #d
    'estimated': 'e', #e
    'f': 'f', #f
}

data = open("filter-font7.ttx","r").readlines()

result = ""

fail = []

for x in data:
    try:
        result += str(map_key[x.strip()])
    except:
        fail.append(x)
        continue


print(result)
