from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long

data = [b'\xe7M\xde\xa1\x13\x8c>\x0f\x0c\x02\xc7<\x9aF\x95\xc2\xa1\x90\xa4\x93sEa\xd9\xbd\xdc\x01\xf6O\xc3\x01Y\x89\x12\xba\x03]\xf6\x97h\xa6\xb9L\xbd\x1b\xfb\xba\x90\xaf\xdf\x90\xe2+\xae3\x06Q\x83\xc1\xe5\x94\x92\xb8\xfas\x8b\x1d\xbdb\x93\x93\x07\x12T\x8f3#\x01\xd3w\xd7\x96\xeaV\xae)d\x84W#\xd5\x97\xc5~\xb4\x0b);\xbd\xfd,Lg\x8bZ\x0b\x8f u\n|9\x0b@p\x05F\xf8+QDHQg\xfc\xbb\x05.', 174074464316835538482184680001658192242410825388376907636477842824191443684645308228203233974220832188117583297191087613707209445376372476904969987329345257218523073605475609089019124992042210016457959240271656826017315704293319015244687378364557458668679822645340657844143376734558755181517726112992266293641]

n = data[1]
c = bytes_to_long(data[0])
cp = n + c
e = 65537

# Calculate the modular inverse of e modulo (n-1)
#d = inverse(e, n-1)
d = 100922125611219358838047043675221701824048121236198925531464853684910479488560403000424341640363378546770766055206563696391643347826733732585886440309532056598181221366764594701410968967112254326339878531110088541760439560863770836370861370345602105674278019153033609036819990881582838120099295381071061386593

a = pow(cp, d, n)

print(long_to_bytes(a).decode())

