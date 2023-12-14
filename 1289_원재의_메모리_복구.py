T = int(input())
for tc in range(1, T+1):

    origin = list(map(int, input()))
    mistake = [0] * len(origin)

    cnt = 0

    for i in range(len(origin)):
        if origin[i] != mistake[i]:
            for k in range(i, len(origin)):
                mistake[k] = origin[i]
            cnt += 1
                # break

    print(f'#{tc} {cnt}')


