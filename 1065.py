def get_1_10(n, m):
    if n == 3:
        return m%10, m//10%10, m//100
    elif n == 4:
        return m%10, m//10%10, m//100%10, m//1000

n = int(input())
count = 0

for i in range(1, n+1):
    if i < 100:
        count += 1
    elif i < 1000:
        temp_num = i
        num1, num10, num100 = get_1_10(3, temp_num)
        if num1 - num10 == num10 - num100:
            count += 1

print(count)