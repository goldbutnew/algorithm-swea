T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 10x10 빈 배열 생성
    empty_canvas = [[0] * 10 for _ in range(10)]

    for add_canvas in range(N):
        arr = list(map(int, input().split()))

        # print(arr)
        start_x = arr[0]
        start_y = arr[1]
        end_x = arr[2]
        end_y = arr[3]
        color = arr[4]

        # 1, 2로 칠하기
        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                empty_canvas[i][j] += color

        result = 0
        for i in range(10):
            for j in range(10):
                if empty_canvas[i][j] == 3:
                    result += 1

    print(f'#{tc} {result}')