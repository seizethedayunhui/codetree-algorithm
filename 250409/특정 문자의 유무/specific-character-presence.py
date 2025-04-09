string = input()

ee_flag = False
ab_flag = False

for i in range(len(string)-2) :
    ee_string = str()
    ab_string = str()
    for j in range(i, i+2) :
        ee_string += string[j]
        ab_string += string[j]
    if ee_string.lower() == "ee":
        ee_flag = True
    if ab_string.lower() == "ab" :
        ab_flag = True

if ee_flag :
    print("Yes", end=" ")
else :
    print("No", end=" ")

if ab_flag :
    print("Yes")
else :
    print("No")
        
        