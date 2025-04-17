N = int(input())

N_list = list(map(int, input().split()))

def print_number(arr) :
    for elem in arr :
        if elem % 2 :
            print(elem, end=" ")
        else :
            print(int(elem/2), end=" ")

print_number(N_list)