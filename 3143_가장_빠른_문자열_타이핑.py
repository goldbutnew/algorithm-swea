T = int(input())

for tc in range(1, T + 1):
    sentence, mini = map(str, input().split())

    count = 0

    new_sentence = sentence.replace(mini, 'A')

    for i in new_sentence:
        count += 1

    # print(new_sentence)

    print(f'#{tc} {count}')