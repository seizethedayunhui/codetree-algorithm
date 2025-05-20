input_string = input()
input_list = list()

# 리스트에 input 하기
for elem in input_string :
    input_list.append(elem)

cnt = 0

for i in range(len(input_list)):
    if input_list[i] == "(" :
        for j in range(i+1, len(input_list)):
            if input_list[j] == ")" :
                cnt +=1

print(cnt)


