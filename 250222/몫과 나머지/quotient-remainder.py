import math
a, b = input().split()

a = int(a)
b = int(b)

print(f"{math.floor(a / b)}...{a % b}")