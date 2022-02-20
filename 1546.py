n = int(input())
num_list = list(map(int, input().split()))
new_list = []
m = max(num_list)

for i in range(0, len(num_list)):
    new_list.append(num_list[i] / m * 100)

new_average = sum(new_list) / n
print(new_average)