N = int(input())

arr = [0] * 10000

idx = 0 # 현재 삽입할 위치! 따라서, 현재는 idx-1 만큼 차있음. 

for i in range(N) :

    cmd = input().split()
    
    if cmd[0] == "push" :
        arr[idx] = int(cmd[1])
        idx += 1
    
    elif cmd[0] == "size" :
        print(idx)

    elif cmd[0] == "empty" :
        if not idx :
            print(1)
        else :
            print(0)

    elif cmd[0] == "pop" :
        idx -= 1
        print(arr[idx])
        

    elif cmd[0] == "top" :
        print(arr[idx-1])