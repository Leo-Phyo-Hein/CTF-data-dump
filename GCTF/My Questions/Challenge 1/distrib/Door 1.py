import binascii

key = 269993421122124259710412044007159979234006209960578
access = " "

def passwordCheck(password):
    a = ''.join(format(ord(i), '08b') for i in password)
    b = bin(key)
    aList = list(a)
    bList = list(b)
    bList.pop(0)
    bList.pop(0)

    if (len(aList) != len(bList)):
        access = "Access Denied"
        return access

    for i in range(len(aList)):
        if (int(aList[i], base=2) ^ int(bList[i], base=2) != 1):
            access = "Access Denied"
            return access
    access = "Access Granted"
    return access

def main():
    userInput = input("Enter the password: ")
    print(passwordCheck(userInput))

if __name__ == "__main__":
    main()
