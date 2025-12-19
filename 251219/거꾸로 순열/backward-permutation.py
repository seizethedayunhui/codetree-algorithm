N = int(input())

arr = list()
visited = [ False for _ in range(N+1) ]
def print_per() :

    for i in range(N) :
        print(arr[i], end=" ")
    print()

def make_reverse_per() :

    if len(arr) == N :
        print_per()
        return
    
    for i in range(N, 0, -1) :

        if visited[i] :
            continue

        arr.append(i)
        visited[i] = True

        make_reverse_per()

        arr.pop()
        visited[i] = False

make_reverse_per()

    