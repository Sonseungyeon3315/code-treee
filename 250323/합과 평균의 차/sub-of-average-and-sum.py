numbers = list(map(int,input().split()))

total = sum(numbers)
average = total // len(numbers)
res = total - average

print(total)
print(average)
print(res)