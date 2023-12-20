T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #  1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미
    # 테이블의 윗부분에 N극이 아래부분에 S극이 위치한다고 가정

    # 1일 경우.... 아래 행에 2가 없으면 됨
    # 2일 경우... 위 행에 1이 없으면 됨

    cnt = 0

    # 배열 순회 (열 우선 순회)
    for j in range(N):
        find = 0
        for i in range(N):

            # N극 자석일 경우
            if arr[i][j] == 1:
                find = 1

            # S극 자석일 경우
            if arr[i][j] == 2:
                if find == 1:
                    cnt += 1
                    find = 0

    print(f'#{tc} {cnt}')