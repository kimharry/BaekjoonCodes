test = int(input())
result = []

for i in range(0, test):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    squared_distance = (x1 - x2) ** 2 + (y1 - y2) ** 2

    if squared_distance == 0 and r1 == r2:
        result.append(-1)
    elif squared_distance == (r1 + r2) ** 2 or squared_distance == abs(r1 - r2) ** 2:
        result.append(1)
    elif abs(r1 - r2) ** 2 < squared_distance < (r1 + r2) ** 2:
        result.append(2)
    else:
        result.append(0)

for i in range(0, len(result)):
    print(result[i])
