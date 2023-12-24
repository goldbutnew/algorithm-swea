for tc in range(10):
    tc_num = int(input())
    N = 100
    ladder_matrix = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

    # 좌, 우, 위 탐색 초기값 설정
    now_row = 99

    # row=99에서 col=2일 때의 col 값을 now_col로 설정
    for col in range(N):
        if ladder_matrix[99][col] == 2:
            now_col = col

    # (now_row)-1 하면서 값 탐색
    # 좌우 탐색
    while now_row >= 0 and 0 <= now_col <= 100:

        if ladder_matrix[now_row][now_col - 1] == 1:
            while ladder_matrix[now_row][now_col - 1] != 0:
                now_col -= 1
            now_row -= 1

        elif ladder_matrix[now_row][now_col + 1] == 1:
            while ladder_matrix[now_row][now_col + 1] != 0:
                now_col += 1
            now_row -= 1

        else:
            now_row -= 1

    print(f'#{tc_num} {now_col - 1}')