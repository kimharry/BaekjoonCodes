a = int(input())
b = int(input())
c = int(input())
num = a * b * c
num_list = [0 for _ in range(0, 10)]

while num != 0:
    temp = num % 10
    for i in range(0, 10):
        if i == temp:
            num_list[i] += 1
    num = num // 10

for i in range(0, 10):
    print(num_list[i])
