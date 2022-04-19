import math

x = int(input())

sigma = 1 / (1 + math.pow(math.e, -1 * x))

print(round(sigma, 2))