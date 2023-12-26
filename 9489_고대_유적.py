T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for M in range(N)]

    max_v = 0

    # 행 우선 탐색
    for row in range(N):
        count = 0
        for j in range(M):
            if arr[row][j] == 1:
                count += 1
                if count > max_v:
                    max_v = count
            elif arr[row][j] == 0:
                if count > max_v:
                    max_v = count
                count = 0

    # 열 우선 탐색
    for col in range(M):
        count = 0
        for i in range(N):
            if arr[i][col] == 1:
                count += 1
                if count > max_v:
                    max_v = count
            elif arr[i][col] == 0:
                if count > max_v:
                    max_v = count
                count = 0

    print(f'#{tc} {max_v}')