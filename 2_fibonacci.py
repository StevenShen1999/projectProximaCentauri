dp = [1, 2]
result = 2

while True:
    curr = dp[-1] + dp[-2]
    if (curr > 4000000):
        break
    if (curr & 1 == 0):
        result += curr
    dp = [dp[-1], curr]

print(result)