n = int(input())
result = []

for k in range(0, n):
    p, s = input().split()
    p = int(p)
    result.append([])
    for i in range(0, len(s)):
        for j in range(0, p):
            result[k].append(s[i])
    result[k] = ''.join(result[k])

for i in range(0, n):
    print(result[i])