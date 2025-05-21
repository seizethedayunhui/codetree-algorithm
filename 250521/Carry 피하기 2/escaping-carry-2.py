N = int(input())

nums = list()

for _ in range(N) :
    nums.append(int(input()))

def check_carry(nums) :

    num_elem = list()

    while nums > 0 :

        num_elem.append(nums % 10)
        nums //= 10

    return num_elem

def check_sum_carry(num1, num2) :

    num1_elem = check_carry(num1)
    num2_elem = check_carry(num2)

    elem_len = min(len(num1_elem), len(num2_elem))

    for i in range(elem_len) :
        if (num1_elem[i] + num2_elem[i]) >= 10 :
            return False

    return True
        

max_sum = 0
for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N):

            three_sum = nums[i] + nums[j] + nums[k]

            if check_sum_carry(nums[i], nums[j]) and check_sum_carry(nums[i]+nums[j], nums[k]) :
                max_sum = max(max_sum, three_sum)

if max_sum :
    print(max_sum)
else :
    print(-1)

