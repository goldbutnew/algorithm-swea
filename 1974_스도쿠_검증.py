T = int(input())
for tc in range(1, T + 1):

    # 스도쿠판은 9 * 9 배열
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 3 * 3 검증할 때 필요한 델타 선언
    di = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dj = [0, 1, 2, 0, 1, 2, 0, 1, 2]

    # row * 9 검증
    for row in range(9):
        s = 0
        for j in range(9):
            s += arr[row][j]
        if s == 45:
            ans = 1
        else:
            ans = 0
            break

    # 9 * col 검증
    for col in range(9):
        s = 0
        for i in range(9):
            s += arr[i][col]
        if s == 45 and ans == 1:
            ans = 1
        else:
            ans = 0
            break

    # 3 * 3 검증
    for row in range(3):
        start_x = 3 * row
        for col in range(3):
            start_y = 3 * col
            s = 0
            for k in range(9):
                ni, nj = start_x + di[k], start_y + dj[k]
                s += arr[ni][nj]
            if s == 45 and ans == 1:
                ans = 1
            else:
                ans = 0
                break

    print(f'#{tc} {ans}')