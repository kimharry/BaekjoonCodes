h, m = map(int, input().split())
cook = int(input())

m += cook
if m >= 60:
    h += m // 60
    m = m % 60

if h >= 24:
    h = h % 24

print(h, m)
