def paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return paper(N - 10) + paper(N - 20) * 2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    ans = paper(N)

    print(f'#{tc} {ans}')