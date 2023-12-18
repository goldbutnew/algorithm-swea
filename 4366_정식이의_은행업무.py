T = int(input())

for tc in range(1, T + 1):

    bin_exp = input()
    trit_exp = input()

    dec = []

    for i in range(len(bin_exp)):
        tmp = list(bin_exp)
        if tmp[i] == '0':
            tmp[i] = '1'
            changestr = ''.join(tmp)
            dec.append(int(changestr, 2))

        elif tmp[i] == '1':
            tmp[i] = '0'
            changestr = ''.join(tmp)
            dec.append(int(changestr, 2))

    num = ['0', '1', '2']

    for i in range(len(trit_exp)):

        tmp = list(trit_exp)

        if tmp[i] == '0':
            for k in num:
                tmp[i] = k
                t = ''.join(tmp)
                if int(t, 3) in dec:
                    ans = int(t, 3)

        elif tmp[i] == '1':
            for k in num:
                tmp[i] = k
                t = ''.join(tmp)
                if int(t, 3) in dec:
                    ans = int(t, 3)

        elif tmp[i] == '2':
            for k in num:
                tmp[i] = k
                t = ''.join(tmp)
                if int(t, 3) in dec:
                    ans = int(t, 3)

    print(f'#{tc} {ans}')