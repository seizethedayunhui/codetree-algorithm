N, M, p = map(int, input().split())
messages = list()

for _ in range(M) :
    people, cnt = input().split()
    cnt = int(cnt)
    messages.append([people, cnt])

members = [ chr(i + 65) for i in range(N)]

exist_members = list()
for i in range(p-1, M) :
    exist_members.append(messages[i][0])

not_read_members = list()
for member in members :
    flag = False
    for exist_member in exist_members :
        if member == exist_member :
            flag = True
            break
    
    if not flag :
        not_read_members.append(member)

for member in not_read_members :
    print(member, end=" ")


    