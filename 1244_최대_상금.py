def counting(cnt):
    global max_num
    global used

    t = int(''.join(num_info))

    c_t = [cnt, t]

    if c_t in used:
        return
    else:
        used.append(c_t)

    if cnt == exchange:
        if t > max_num:
            max_num = t
        return

    for i in range(N):
        for j in range(i + 1, N):
            num_info[i], num_info[j] = num_info[j], num_info[i]
            counting(cnt + 1)
            num_info[j], num_info[i] = num_info[i], num_info[j]


T = int(input())

for tc in range(1, T + 1):
    nums, exchange = list(map(int, input().split()))
    num_info = []

    for num in str(nums):
        num_info.append(num)

    N = len(num_info)
    max_num = 0
    cnt = 0
    used = []

    counting(cnt)

    print(f'#{tc} {max_num}')