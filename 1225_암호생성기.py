T = 10

for tc in range(1, T + 1):
    tc_num = int(input())
    data8 = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        t = data8.pop(0) - i
        if t <= 0:
            data8.append(0)
            break
        data8.append(t)
        i += 1

    print(f'#{tc_num}', end=" ")
    print(*data8)