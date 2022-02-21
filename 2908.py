num_list = list(input().split())
num1 = list(num_list[0])
num2 = list(num_list[1])
num1.reverse()
num2.reverse()

if num1 > num2:
    print(num1[0] + num1[1] + num1[2])
else:
    print(num2[0] + num2[1] + num2[2])