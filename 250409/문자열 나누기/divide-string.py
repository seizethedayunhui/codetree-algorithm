n = int(input())

num_list = list(input().split())

num_string = "".join(num_list)

for i in range(len(num_string)) :
    if (i+1) % 5 :
        print(num_string[i], end="")
    
    else :
        print(num_string[i])