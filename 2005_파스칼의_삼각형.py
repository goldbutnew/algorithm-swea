T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 계산에 사용할 임시 리스트
    tmp = []

    # 출력할 최종 리스트
    tri = []

    print(f'#{tc}')

    for i in range(1, N + 1):
        # 매 행의 첫째줄은 1이 들어감
        # i = 2가 되기 전까지는 계속 임시 리스트에 1추가
        tmp.append(1)
        tri.append(1)

        if i < 2:
            pass
        elif 2 <= i:
            for j in range(1, len(tri) - 1):
                tmp[j] = tri[j] + tri[j - 1]

        for j in range(len(tri)):
            tri[j] = tmp[j]
            print(str(tri[j]) + " ", end="")

        print("")