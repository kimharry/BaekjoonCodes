n, x = map(int, input().split())
temp = []
temp = list(map(int, input().split()))
result = []

for i in range(0, n):
    if temp[i] < x:
        result.append(temp[i])

for i in range(0, len(result)):
    print(result[i], end=" ")