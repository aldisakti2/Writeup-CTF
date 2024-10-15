from Crypto.Util.number import getPrime, bytes_to_long
from secret import message, x, y

p = getPrime(y)
n = p ** x
e = 0x10001
c = pow(bytes_to_long(message), e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")

# output
# n = 174398141961264126560505296048651397103940625972358808906187816452656090815275082092703206639204234732453380366400438429846076789218559828669690390572528240520254507036152659026582129125892087219537071916257813880120391483891236016422449795410600212796367274254070440928882993348666993424943717023976062255483456283318813107003678274274454583252439764631805477342477492425052659593801
# e = 65537
# c = 38415069832658278102412940476349224522223117826717864236716063942465292251639452037471899276433883280487660575851320701796429668476551053062015248611453285019543570394965516221325993414456754832832080360042304547277452474428650298929639938371072386565545457564351801474854761480051602266412901190322297685878637385354294132832534425751762322767659303351614194618177802401960510283943