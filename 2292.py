n = int(input())

sum = 1
i = 1
while sum < n:
    sum += 6 * i
    i += 1

if n == 1:
    print(1)
else:
    print(i)
