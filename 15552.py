import sys

t = int(input())

for _ in range(0, t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)