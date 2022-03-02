fixed, change, price = map(int, input().split())
n = 0

if change >= price:
    print(-1)
else:
    print(fixed // (price - change) + 1)