word = input()
word = list(word)
time = 0

for i in range(0, len(word)):
    if 'A' <= word[i] <= 'C':
        time += 3
    elif 'D' <= word[i] <= 'F':
        time += 4
    elif 'G' <= word[i] <= 'I':
        time += 5
    elif 'J' <= word[i] <= 'L':
        time += 6
    elif 'M' <= word[i] <= 'O':
        time += 7
    elif 'P' <= word[i] <= 'S':
        time += 8
    elif 'T' <= word[i] <= 'V':
        time += 9
    elif 'W' <= word[i] <= 'Z':
        time += 10

print(time)
