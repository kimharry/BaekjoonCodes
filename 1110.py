def get_1_10(n):
    return n % 10, n // 10

original = int(input())
num = original
num1, num10 = get_1_10(num)

i = 0

while True:
    i += 1
    num1, num10 = get_1_10(num)
    new_num1, _ = get_1_10(num1 + num10)
    num = num1 * 10 + new_num1
    if num == original:
        break

print(i)