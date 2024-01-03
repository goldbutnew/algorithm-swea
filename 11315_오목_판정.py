# 오목 확인
def check(arr):
    cnt = 0

    # 행 탐색
    for i in range(N):
        row_total = 0
        for j in range(N):
            row_total += arr[i][j]
            if row_total < 5 and arr[i][j] == 0:
                row_total = 0
            elif row_total == 5:
                cnt += 1

    # 열 탐색
    for j in range(N):
        col_total = 0
        for i in range(N):
            col_total += arr[i][j]
            if col_total < 5 and arr[i][j] == 0:
                col_total = 0
            elif col_total == 5:
                cnt += 1

    # 대각선 탐색
    # \ 방향의 합
    for i in range(N):
        for j in range(N):
            rd_total = 0
            if arr[i][j] == 1:
                for k in range(5):
                    if 0 <= i + k < N and 0 <= j + k < N:
                        rd_total += arr[i + k][j + k]
                        if rd_total < 5 and arr[i + k][j + k] == 0:
                            rd_total = 0
                        elif rd_total == 5:
                            cnt += 1

    # / 방향 합
    for i in range(N):
        for j in range(N):
            ld_total = 0
            if arr[i][j] == 1:
                for k in range(5):
                    if 0 <= i + k < N and 0 <= j - k < N:
                        ld_total += arr[i + k][j - k]
                        if ld_total < 5 and arr[i + k][j - k] == 0:
                            ld_total = 0
                        elif ld_total == 5:
                            cnt += 1

    return cnt


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # . -> 0 / O -> 1로 배열 변경
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                arr[i][j] = 1
            elif arr[i][j] == '.':
                arr[i][j] = 0

    if check(arr) >= 1:
        ans = "YES"
    elif check(arr) < 1:
        ans = "NO"

    print(f'#{tc} {ans}')