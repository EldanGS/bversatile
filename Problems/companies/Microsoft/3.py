def solution(N):
    negative = 1
    str_n = str(N)
    max_num = N
    if N < 0:
        negative = -1
        max_num = int('-5' + str_n[1:])
        str_n = str_n[1:]

    for i in range(len(str_n) + 1):
        current_num = str_n[:i] + '5' + str_n[i:]
        max_num = max(max_num, int(current_num) * negative)

    return max_num


