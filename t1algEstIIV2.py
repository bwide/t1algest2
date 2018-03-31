import sys
import itertools

path = sys.argv[1]

color_dict = {} # dont load this huge dict

with open(path) as file:
    file.readline()
    for line in file:
        lineContents = line.split(' ')
        coordinates = [int(x) for x in lineContents[:4]]
        color = lineContents[4].strip('\n')

        rangeX = range(coordinates[0], coordinates[2])
        rangeY = range(coordinates[1], coordinates[3])

        squares = set( itertools.product(rangeX, rangeY) )

        for key in color_dict.keys():
            color_dict[key] -= squares


        if color in color_dict:
            color_dict[color] += squares
        else:
            color_dict[color] = squares

for color in color_dict:
    print(str(color) + ": " + str(len(color_dict[color])))