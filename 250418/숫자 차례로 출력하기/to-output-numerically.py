N = int(input())

def print_num1(N):
    
    if N == 0 :
        return
    print_num1(N-1)
    print(N, end=" ")


def print_num2(N):

    if N == 0:
        return
    print(N, end=" ")
    print_num2(N-1)


print_num1(N)
print()
print_num2(N)