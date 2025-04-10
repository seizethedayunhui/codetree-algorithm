S, Q = input().split() # 문자열과 질의 개수

Q_list = list()
S_list = list(S)

for _ in range(int(Q)) :
    question = list(input().split())
    Q_list.append(question) # 질문 추가하기

# 질의 1를 수행하는 함수
def question1 (a, b, S_list) :
    temp = S_list[a-1]
    S_list[a-1] = S_list[b-1]
    S_list[b-1] = temp

# 질의 2를 수행하는 함수
def question2 (x, y, S_list) :
    for i in range(len(S_list)) :
        if S_list[i] == x :
            S_list[i] = y
 
for i in range(int(Q)) :
    if int(Q_list[i][0]) == 1 :
        question1(int(Q_list[i][1]), int(Q_list[i][2]), S_list)
    else :
        question2(Q_list[i][1], Q_list[i][2], S_list)
    print("".join(S_list)) 