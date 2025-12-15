N = int(input())

seq = list()

# s_length - 최대 길이
# length_idx - 현재 길이
# def check_all_condi(s, s_max_length, s_current_length) :

#     if s_current_length == s_max_length + 1:
#         return True

#     # 중복 체크 시작 인덱스
#     idx_range = len(s) - (s_current_length * 2) + 1
#     for i in range(idx_range) :
#         if not check_condi(s, i, 0, s_current_length) :
#             return False

#     return check_all_condi(s, s_max_length, s_current_length + 1)

# # start - 시작 인덱스
# # idx - 길이 인덱스
# # length 검사 중인 길이
# def check_condi(s, start, idx, length) :

#     if (s[start : start + length] == s[start + length : start + 2 * length]) :
#         return False
#     else :
#         return True


def check_part_condi(s) :

    original_len = len(s)
    possi_part_len = len(s) // 2 + 1

    for i in range(1, possi_part_len) :
        if s[original_len - i:] == s[original_len - 2*i : original_len - i] :
            return False
        
    return True

def make_seq(idx, s) :

    # if len(s) % 2 :
    #     s_length = len(s) // 2 + 1
    # else :
    #     s_length = len(s) // 2

    # if not check_all_condi(s, s_length, 1)  :
    #     return

    if idx == N :
        seq.append(s)
        return

    for i in range(4, 7) :
        s += str(i)

        if check_part_condi(s) :
            make_seq(idx + 1, s)
        s = s[:idx]

s = ""
make_seq(0, s)
print(int(seq[0]))
