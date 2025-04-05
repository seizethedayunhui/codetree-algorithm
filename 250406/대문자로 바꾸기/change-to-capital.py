char_arr = [ list(map(str, input().split())) for _ in range(5) ]

for char_list in char_arr :
    for i in range(3) :
        # ord() : 문자열을 수로 바꿔주는 함수
        print(chr(ord(char_list[i])-32), end=" ")
    print()