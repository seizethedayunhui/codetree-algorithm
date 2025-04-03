N = int(input())
num_list = list(map(int, input().split()))

even_list = list()

for num in num_list :
    if num % 2 == 0 :
        even_list.append(num)

for even in even_list :
    print(even, end=" ")