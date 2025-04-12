cnt = 0

string_list = list()

while True :

    string = input()

    if string == '0' :
        print(cnt)
        for stirng in string_list :
            print(stirng)
        break
    else :
        if not ( cnt % 2 ) :
            string_list.append(string)
        cnt += 1
