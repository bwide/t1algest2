import sys
import itertools

#SETUP
path = sys.argv[1]

dict = {}
with open(path) as file:
    file.readline()
    for line in file:
        lineContents = line.split(' ')
        coordinates = [int(i) for i in lineContents[:4]]
        color = lineContents[4].strip('\n')
        
        rangeX = range(coordinates[0], coordinates[2])
        rangeY = range(coordinates[1], coordinates[3])
        
        for coordinate in itertools.product(rangeX, rangeY):
            dict[coordinate] = color

colorCount = {}

for coordinate, color in dict.items():
    if color in colorCount:
        colorCount[color] += 1
    else:
        colorCount[color] = 1

for color in colorCount: print(color + ": " + str(colorCount[color]))