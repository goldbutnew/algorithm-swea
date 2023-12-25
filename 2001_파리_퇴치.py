T = int(input())

for tc in range(1, T + 1):

    # 1차원 배열로 N, M을 받는다
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]

    # N*N 배열 생성
    big_arr = [list(map(int, input().split())) for _ in range(N)]

    # 좌표 찾기
    # big_arr의 값을 kill_fly에 넣어 주기

    # 초기값 선언
    max_kill_fly = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 초기값 선언
            kill_fly = 0
            for i2 in range(M):
                for j2 in range(M):
                    kill_fly += big_arr[i + i2][j + j2]

            if kill_fly > max_kill_fly:
                max_kill_fly = kill_fly

    print(f'#{tc} {max_kill_fly}')