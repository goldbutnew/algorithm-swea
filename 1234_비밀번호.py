T = 10
for tc in range(1, T + 1):
    N, string = list(map(str, input().split()))

    # print(N)
    # print(string)

    # 스택 생성
    stack = []

    # 문자열을 순회
    for char in string:
        # stack and: 스택의 존재 여부 판별
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    ans = "".join(stack)

    print(f'#{tc} {ans}')