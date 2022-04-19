import math


value = int(input())
base = int(input())

if base > 1:
    result = math.log(value, base)
else:
    result = math.log(value)

print(round(result, 2))
