N, M, p = map(int, input().split())
messages = list()

for _ in range(M) :
    people, cnt = input().split()
    cnt = int(cnt)
    messages.append([people, cnt])

members = [ chr(i + 65) for i in range(N)]

exist_members = list()

# 모두 읽은 경우 exist_members에 모두 포함시킴. 
if messages[p-1][1] > 0 :
    for i in range(p-1, M) :
        exist_members.append(messages[i][0])
else :
    for i in range(N) :
        exist_members.append(chr(i + 65))

# 읽지 않은 멤버들을 찾아내는 리스트
not_read_members = list()
for member in members :
    flag = False
    for exist_member in exist_members :
        if member == exist_member :
            flag = True
            break
    
    if not flag :
        not_read_members.append(member)

# 출력
for member in not_read_members :
    print(member, end=" ")


    