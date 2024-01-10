T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for M in range(N)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    max_v = 0

    # 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임

    for i in range(N):
        for j in range(M):
            sum_v = arr[i][j]
            for k in range(4):
                # ni, nj = i + di[k], j + dj[k]
                for n in range(1, arr[i][j] + 1):
                    x = i + di[k] * n
                    y = j + dj[k] * n
                    if 0 <= x < N and 0 <= y < M:
                        sum_v += arr[x][y]

            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')