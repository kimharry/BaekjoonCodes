n = int(input())

sum = 0
i = 1
while sum + i < n:
    sum += i
    i += 1

temp = n - sum

if i % 2 == 1:
    print(str(i-temp+1) + "/" + str(temp))
else:
    print(str(temp) + "/" + str(i-temp+1))