T = int(input())
for tc in range(1, T + 1):
    # 높이 H, 너비 W
    H, W = map(int, input().split())

    # 게임 맵은 H * W 크기의 격자판
    # H개의 각각의 줄에는 길이가 W인 문자열
    game_map = [list(input()) for _ in range(H)]

    # 사용자가 넣을 입력의 개수 N
    N = int(input())

    # 길이가 N인 문자열
    my_string = input()

    x = 0
    y = 0
    dir = ""

    # 전차의 초기값 찾기
    for i in range(H):
        for j in range(W):
            if game_map[i][j] == '^':
                x = i
                y = j
                dir = '^'
                break
            elif game_map[i][j] == '>':
                x = i
                y = j
                dir = '>'
            elif game_map[i][j] == '<':
                x = i
                y = j
                dir = '<'
            elif game_map[i][j] == 'v':
                x = i
                y = j
                dir = 'v'
            else:
                pass

    # print(x)
    # print(y)
    # print(game_map[x][y])

    for k in range(N):
        if 0 <= x < H and 0 <= y < W:
            # and 0 <= x-1 < H and 0 <= y-1 < W and 0 <= x+1 < H and 0 <= y+1 < W
            if my_string[k] == 'U':
                game_map[x][y] = '^'
                if 0 <= x - 1 < H and game_map[x - 1][y] == '.':
                    game_map[x - 1][y] = '^'
                    game_map[x][y] = '.'
                    x = x - 1

            elif my_string[k] == 'D':
                game_map[x][y] = 'v'
                if 0 <= x + 1 < H and game_map[x + 1][y] == '.':
                    game_map[x + 1][y] = 'v'
                    game_map[x][y] = '.'
                    x = x + 1

            elif my_string[k] == 'L':
                game_map[x][y] = '<'
                if 0 <= y - 1 < W and game_map[x][y - 1] == '.':
                    game_map[x][y - 1] = '<'
                    game_map[x][y] = '.'
                    y = y - 1

            elif my_string[k] == 'R':
                game_map[x][y] = '>'
                if 0 <= y + 1 < W and game_map[x][y + 1] == '.':
                    game_map[x][y + 1] = '>'
                    game_map[x][y] = '.'
                    y = y + 1
                    # print(y)
                    # print(game_map[x][y])

            elif my_string[k] == 'S':

                if game_map[x][y] == '>':
                    for j in range(y + 1, W):
                        if game_map[x][j] == '#':
                            break
                        if game_map[x][j] == '*':
                            game_map[x][j] = '.'
                            break

                elif game_map[x][y] == '<':
                    for j in range(y - 1, -1, -1):
                        if game_map[x][j] == '#':
                            break
                        elif game_map[x][j] == '*':
                            game_map[x][j] = '.'
                            break

                elif game_map[x][y] == '^':
                    for i in range(x - 1, -1, -1):
                        if game_map[i][y] == '#':
                            break
                        elif game_map[i][y] == '*':
                            game_map[i][y] = '.'
                            break

                elif game_map[x][y] == 'v':
                    for i in range(x + 1, H):
                        if game_map[i][y] == '#':
                            break
                        elif game_map[i][y] == '*':
                            game_map[i][y] = '.'
                            break

    print(f'#{tc}', end=' ')  # 테스트 케이스 번호 출력

    # 첫 번째 행 출력
    print(''.join(map(str, game_map[0])))

    # 나머지 행 출력
    for row in game_map[1:]:
        print(''.join(map(str, row)))