num_list = []
for i in range(0, 10):
    temp = int(input())
    num_list.append(temp % 42)

count = 0
count_list = []
for i in range(0, 10):
    if num_list[i] in count_list:
        continue
    else:
        count_list.append(num_list[i])
        count += 1


print(count)
