N = int(input())

seq = list()

# s_length - 최대 길이
# length_idx - 현재 길이
def check_all_condi(s, s_max_length, s_current_length) :

    if s_current_length == s_max_length + 1:
        return True

    # 중복 체크 시작 인덱스
    idx_range = len(s) - (s_current_length * 2) + 1
    for i in range(idx_range) :
        if not check_condi(s, i, 0, s_current_length) :
            return False

    return check_all_condi(s, s_max_length, s_current_length + 1)

# start - 시작 인덱스
# idx - 길이 인덱스
# length 검사 중인 길이
def check_condi(s, start, idx, length) :

    if idx == length :
        return False

    if (s[start + idx] == s[start + length + idx]) :
        return check_condi(s, start, idx+1, length)
    else :
        return True

def make_seq(idx, s) :

    if idx == N :
        #print(s)
    
        if len(s) % 2 :
            s_length = len(s) // 2 + 1
        else :
            s_length = len(s) // 2

        if check_all_condi(s, s_length, 1) :
            seq.append(s)
        #seq.append(s)
        return

    for i in range(4, 7) :
        s += str(i)
        make_seq(idx + 1, s)
        s = s[:idx]

s = ""
make_seq(0, s)
print(int(seq[0]))
