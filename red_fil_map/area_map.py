import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def area(r):
    """ Area of circle with radius 'r' """
    return math.pi * (r**2)


radius = [2, 3, 7.1, 0.4, 14]

# Direct method without using map function

areas = []
for r in radius:
    a = area(r)
    areas.append(a)

# Use of - map function

areas2 = map(area, radius)

temperatures_cities = [("Berlin", 29), ("Prage", 20),
                       ("London", 18), ("Los Angeles", 30), ("Tokyo", 25)]


def from_C_to_F(data): return (data[0], (9/5)*data[1]+32)


map_temp = list(map(from_C_to_F, temperatures_cities))


if __name__ == '__main__':
    print(areas)
    print(areas2)
    print(bcolors.WARNING + "Map function creates map object (iterator over results) we need to transform it to list" + bcolors.ENDC)
    print(list(areas2))
    print("Temperatures in cities [Fahrenheit]")
    print(map_temp)
