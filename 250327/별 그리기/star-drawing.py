N = int(input())

for i in range(N) :
    for _ in range(N-i-1):
        print(" ", end="")
    for _ in range(2*i+1):
        print("*", end="")
    for _ in range(N-i+1):
        print("", end="")
    print()


for j in range(N-1):
    for _ in range(j+1):
        print(" ", end="")
    for _ in range((2*N-1)-2*(j+1)):
        print("*", end="")
    for _ in range(j+1):
        print(" ", end="")
    print()