T = int(input())

for tc in range(1, T + 1):
    code = input()

    top_stack = []

    # 왼쪽 괄호를 스택에 삽입
    for i in range(len(code)):
        if code[i] == '(':
            top_stack.append(code[i])
        elif code[i] == '{':
            top_stack.append(code[i])

    # 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제
    for i in range(len(code)):
        if code[i] == ')':
            top_stack.pop()

        elif code[i] == '}':
            top_stack.pop()

        # top_stack의 len이 0일 경우, 그 리스트는 빈 리스트 -> 다 짝이 맞아서 제거됨
    if len(top_stack) == 0:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')