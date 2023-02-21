import math


def degree_to_radian(degrees):
    return degrees * (math.pi / 180)


degree_value = 15
radian_value = degree_to_radian(degree_value)
print(f"{degree_value} degrees = {radian_value:.6f} radians")
