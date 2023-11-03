T = int(input())

for tc in range(1, T + 1):
    # 도시의 크기 N 하나의 집이 지불할 수 있는 비용 M
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # K의 최대값은?
    K = (N + 1) // 2
    # 비용
    cost = K * K + (K - 1) * (K - 1)
    # (보안 회사의 이익) = (집을 통해 얻는 수익) - (운영 비용)
    # profit = cnt * M - cost
    # 이익이 최댓값일 때?
    max_p = 0

    # 마름모 중심점 기준으로, (K-1) 거리 내에 있는 집들은 계산에서 포함된다

    homes = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                homes.append([i, j])
            else:
                pass

    max_cnt = 0

    for k in range(1, N + 2):
        cost = k * k + (k - 1) * (k - 1)
        for i in range(N):
            for j in range(N):
                tmp_cnt = 0
                for l in range(len(homes)):
                    x = homes[l][0]
                    y = homes[l][1]
                    if abs(i - x) + abs(j - y) < k:
                        tmp_cnt += 1
                if tmp_cnt * M - cost >= 0:
                    if tmp_cnt > max_cnt:
                        max_cnt = tmp_cnt

    print(f'#{tc} {max_cnt}')