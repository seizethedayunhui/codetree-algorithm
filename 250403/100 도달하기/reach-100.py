n = int(input())

first = 1
second = n

print(f"{first} {second}", end=" ")

while True :

    ans = first + second
    print( ans, end=" ")
    
    first = second
    second = ans

    if ans > 100 :
        break
