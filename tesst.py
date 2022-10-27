import math

point = (10, 10)

rect = (20, 20, 40, 40)

rx = (rect[0] + rect[2]) / 2
ry = (rect[1] + rect[3]) / 2
rwidth = rect[2] - rect[0]
rheight = rect[1] - rect[3]

dx = math.fabs(point[0] - rx) - rwidth / 2.0
dy = math.fabs(point[1] - ry) - rheight / 2.0

print(dx ** 2 + dy ** 2)
