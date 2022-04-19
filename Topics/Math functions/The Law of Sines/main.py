import math

b = 7
C = math.radians(105)
B = math.radians(35)

c = b * math.sin(C) / math.sin(B)
print(round(c, 1))
