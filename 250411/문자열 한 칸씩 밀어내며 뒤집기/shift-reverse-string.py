string, Q = input().split()
Q = int(Q)

for _ in range(Q) :
    req = int(input())
    if req == 1 :
        string = string[1:] + string[0]
    # 가장 뒤에 있는 문자를 제외한 나머지 문자를 한칸씩 밀고 가장 뒤에 있던 문자를 가장 앞으로
    elif req == 2 :
        string = string[-1]+string[0:-1]
    # 문자열 전환
    else :
        new_string = str()
        for i in range(len(string)-1, -1, -1):
            new_string += string[i]
        string = new_string
    print(string)

