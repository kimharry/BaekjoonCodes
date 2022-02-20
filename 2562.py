num_list = []
for i in range(0, 9):
    num_list.append(int(input()))

max_num = max(num_list)
print(max_num)

for i in range(0, 9):
    if num_list[i] == max_num:
        print(i + 1)