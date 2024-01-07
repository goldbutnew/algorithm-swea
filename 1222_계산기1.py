T = 10
for tc in range(1, 1 + T):
    N = int(input())
    susik = input()

    stack = [0] * N
    top = -1

    for x in susik:
        if x not in '+':
            top += 1
            stack[top] = int(x)

        else:
            if x == '+':
                op2 = stack[top]
                top -= 1
                op1 = stack[top]
                top -= 1
                top += 1
                stack[top] = op1 + op2

    ans = stack[0] + stack[-1]

    print(f'#{tc} {ans}')