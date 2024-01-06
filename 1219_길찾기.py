def dfs(start, adj_arr):
    # 준비 단계
    stack = []
    visited = [False] * 100

    # 시작
    v = start
    visited[v] = True
    result = []

    while True:
        is_find = False
        for idx in range(100):
            if adj_arr[v][idx] == 1 and visited[idx] == False:
                stack.append(v)

                # 방문처리
                v = idx
                result.append(v)

                # 방문 여부 체크
                visited[v] = True

                # 이동한 정점을 찾은 경우
                is_find = True
                break

        if is_find == False:
            if len(stack) != 0:
                v = stack.pop()
            else:
                break

    return result


T = 10

for tc in range(1, 1 + T):
    tc_num, E = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    adj_arr = [[0] * 100 for _ in range(100)]

    for idx in range(E):
        x = arr[idx * 2]
        y = arr[idx * 2 + 1]
        adj_arr[x][y] = 1
        # adj_arr[y][x] = 1

    route = dfs(1, adj_arr)

    if 99 in route:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')