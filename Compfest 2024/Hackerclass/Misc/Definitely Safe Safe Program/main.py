"""
Welcome to my first Python program!!!

This program will be able to execute most Python
statements just like the REPL, but I have made sure
to sanitize the input so you won't be able to hack
my computer!!!

But... if you somehow managed to hack my computer
here is a gift from me COMPFEST16{PART1_
"""

__file__ = "Nothing here..."

def safe(s):
    blacklist = ["os", "system", "\\", "(", ")", "io", "subprocess", "Popen", "=", "0", "1", "2", "+", "3", "4", "5", "PART2}","6", "7", "8", "9", "import", "-", "globals", "locals", "vars"]
    return not any(c in s for c in blacklist)


if __name__ == "__main__":
    while True:
        cmd = ascii(input(">>> "))
        if not safe(cmd):
            print("Not Allowed!!!")
            continue
            
        result = eval(eval(cmd))
        print(str(result)[:25])