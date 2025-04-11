stirng = input()

for elem in stirng :
    if ord(elem) >= 65 and ord(elem) <= 90 :
        print(elem, end="")
    elif ord(elem) >= 97 and ord(elem) <= 122 :
        print(chr(ord(elem)-32), end="")

