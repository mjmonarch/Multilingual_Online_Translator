import math


edge = int(input())

area = 2 * math.sqrt(3) * math.pow(edge, 2)
volume = math.sqrt(2) * math.pow(edge, 3) / 3

print(f"{round(area, 2)} {round(volume, 2)}")
