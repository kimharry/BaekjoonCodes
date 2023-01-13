result = []
total = int(input())

for _ in range(0, total):
    num_list = list(map(int, input().split()))
    n = num_list.pop(0)
    ave = sum(num_list) / n
    count = 0

    for i in range(0, len(num_list)):
        if num_list[i] > ave:
            count += 1

    result.append(count / n * 100)

for i in range(0, total):
    print("%.3f%%" % result[i])
