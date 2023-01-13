def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)


n = int(input())
score = []

for _ in range(0, n):
    temp = ''
    temp = list(input())
    temp_score = 0

    i = -1
    while i < len(temp):
        i += 1
        k = 1
        if i >= len(temp):
            break
        while temp[i] != 'X':
            temp_score += k
            k += 1
            i += 1
            if i >= len(temp):
                break

    score.append(temp_score)

for i in range(0, n):
    print(score[i])
