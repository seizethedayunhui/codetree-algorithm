N = int(input())

for i in range(N) :
    for _ in range(i):
        print(" ", end=" ")
    for _ in range(2*(N-i)-1):
        print("*", end=" ")
    for _ in range(i):
        print(" ", end=" ")
    print()
for i in range(N-1):
    for _ in range(N-(i+2)) :
        print(" ", end=" ")
    for _ in range(2*(i+1)+1):
        print("*", end=" ")
    for _ in range(N-(i+2)) :
        print(" ", end=" ")
    print()
