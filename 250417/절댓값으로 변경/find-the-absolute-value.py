N = int(input())
N_list = list(map(int, input().split()))

def print_plus_num(arr) :

    for elem in arr :
        print( abs(elem), end=" ")

print_plus_num(N_list)