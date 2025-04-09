string = input()

ee_cnt = 0
eb_cnt = 0
for i in range(len(string)-1) :
   
    ee_str = str()
    eb_str = str()

    for j in range(i, i+2) :
        ee_str += string[j]
        eb_str += string[j]

    
    if ee_str == "ee" :
        ee_cnt += 1

    if eb_str == "eb" :
        eb_cnt += 1

print(ee_cnt, eb_cnt)
