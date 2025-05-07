N = int(input())

# 순위를 저장할 인덱스
num_to_rank = [0] * N 

seq = list()

ori_list = list(map(int, input().split()))


# 시작인덱스 - 값
for i in range(N):
    seq.append((i, ori_list[i]))

seq.sort(key = lambda x : x[1])

for j in range(N):
    num_to_rank[seq[j][0]] = j

for k in range(N):
    print(num_to_rank[k]+1, end=" ")


