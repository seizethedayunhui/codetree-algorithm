char_arr = ['L', 'E', 'B', 'R', 'O', 'S']
char = input()

# 해당 문자열을 찾았는지 확인하는 flag
flag = 0
for i in range(6) :

    # 해당 인덱스의 값과 입력 문자가 같으면 해당 위치 출력 후 종료
    if char_arr[i] == char :
        flag = 1
        print(i)
        break

# 배열에 없는 문자가 주어졌을 경우
if not flag :
    print("None")