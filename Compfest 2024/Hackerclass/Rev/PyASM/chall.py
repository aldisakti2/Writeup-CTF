import sys

def main():
    pw = input('Enter THE password: ')

    if not pw.isalnum():
        print('Password format is not valid!')
        sys.exit()

    if len(pw) > 9:
        print('Password is too long!')
        sys.exit()

    if len(pw) < 9:
        print('Password is too short!')
        sys.exit()

    x = [0] * 9

    for i in range(9):
        x[i] = ord(pw[i]) - 1

    print(x)

    if x[7] + 69 == 120:
        if (x[3] ^ 1337) == 1355:
            if (x[0] // 22) == 5:
                if (x[4] - 16) == 35:
                    if (x[8] << 3) == 832:
                        if (x[1] ** 2) == 9409:
                            if (x[6] * 7) == 693:
                                if ~x[2] == -110:
                                    if x[5] == 107:
                                        print("Correct! Here's your flag: ")
                                        with open('flag.txt') as f:
                                            print(f.read())
                                        sys.exit()

    print('Wrong password.')

if __name__ == "__main__":
    main()


