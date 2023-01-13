word = input()
word = list(word.upper())
word.sort()
i = 0
result = []
breaker = False
is_1 = False

while i < len(word):
    if len(word) == 1:
        is_1 = True
        break
    temp = 0
    if i >= len(word)-1:
        result.append([temp+1, word[i]])
        break
    while word[i+1] == word[i]:
        if i+1 >= len(word)-1:
            temp += 1
            breaker = True
            break
        i += 1
        temp += 1
    result.append([temp+1, word[i]])
    if breaker:
        break
    i += 1

if is_1:
    print(word[0])
else:
    result.sort(reverse=True)
    if result[0][0] == result[1][0]:
        print("?")
    else:
        print(result[0][1])
