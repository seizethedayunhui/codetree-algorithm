n = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

for num in num_list :
    print(num, end=" ")

print()

num_list.sort(reverse=True)

for num in num_list :
    print(num, end=" ")