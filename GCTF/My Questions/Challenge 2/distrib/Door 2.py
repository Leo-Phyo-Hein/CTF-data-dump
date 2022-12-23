import random
import collections

def rand_key(p):
    key = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key += temp
    return(key)

access = " "

def passwordCheck(password):
    a = password
    b = rand_key(4)
    aList = list(a)
    bList = list(b)

    for character in aList:
        if character != '0' and character != '1':
            access = "Access Denied"
            return access

    for i in range(len(aList) - 3):
        register = collections.deque([], 4)
        register.extend(aList[i])
        register.extend(aList[i + 1])
        register.extend(aList[i + 2])
        register.extend(aList[i + 3])

        for j in range(4):
            if (int(register[j], base=2) == int(bList[j], base=2)):
                access = "Access Granted"
            elif (int(register[j], base=2) != int(bList[j], base=2)):
                access = "Access Denied"
                break

        if (access == "Access Granted"):
            return access

    return access

def main():
    userInput = input("Enter the password: ")
    print(passwordCheck(userInput))

if __name__ == "__main__":
    main()
