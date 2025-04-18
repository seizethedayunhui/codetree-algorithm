N = int(input())

def print_num(N):

    if N == 0:
        return
    print(N, end=" ")
    print_num(N-1)
    print(N, end=" ")

print_num(N)