string = input()

for elem in string :

    # 앞은 소문자 범위 뒤는 숫자 범위
    if (ord(elem) >= 97 and ord(elem) <= 122) or (ord(elem) >= 48 and ord(elem) <= 58) :
        print(elem, end="")
    elif ord(elem) >= 65 and ord(elem) <= 90 :
        print(chr(ord(elem)+32), end="")
