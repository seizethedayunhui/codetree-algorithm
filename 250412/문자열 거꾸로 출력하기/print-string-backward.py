for _ in range(10):
    string = input()
    if string == "END" :
        break
    else :
        for i in range(len(string)-1 , -1, -1) :
            print(string[i], end="")
    print()
