T = int(input())

for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]

    new_word = ""
    row_len_lst = []
    max_len = 0

    for i in range(5):
        row_len_lst.append(len(arr[i]))
        if len(arr[i]) > max_len:
            max_len = len(arr[i])

    for j in range(max_len):
        for i in range(len(arr)):
            try:
                new_word += arr[i][j]
            except IndexError:
                pass

    print(f"#{tc} {new_word}")