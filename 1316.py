num = int(input())
count = 0

for i in range(0, num):
    string = input()
    list(string)
    checklist = []
    j = 0
    is_right = True

    while j < len(string):
        if j < len(string) - 1:
            while string[j] == string[j+1]:
                j += 1
                if j+1 == len(string):
                    break
        if string[j] not in checklist:
            checklist.append(string[j])
        else:
            is_right = False
            break
        j += 1

    if is_right:
        count += 1

print(count)
