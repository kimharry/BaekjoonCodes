# 9973
self_number = [i for i in range(1, 10001)]

for i in range(1, 9973):
    num = i
    next_num = num
    while num > 0:
        next_num += num % 10
        num = num // 10

    if next_num in self_number:
        self_number[next_num-1] = 0

for i in range(0, 10000):
    if self_number[i] != 0:
        print(self_number[i])
