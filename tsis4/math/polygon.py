import math


def polygon_area(num_sides, side_length):
    perimeter = num_sides * side_length
    apothem = (side_length / 2) / math.tan(math.pi / num_sides)
    area = 0.5 * perimeter * apothem
    return area


num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = polygon_area(num_sides, side_length)

print("The area of the polygon is:", round(area))
