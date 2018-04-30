import sys
sys.setrecursionlimit(10000)
from pyqtree import Index

path = sys.argv[1]

def size(bbox):
    return (bbox[2]-bbox[0])*(bbox[3]-bbox[1])

def subtract(box1, box2):
    return [box2]


colors = []

with open(path) as file:
    elements = int(file.readline())
    tree = Index(bbox=(0,0,50000,50000))
    for line in file:
        line = line.split(' ')

        bbox = [int(x) for x in line[:4]]
        color = line[4].strip('\n')
        if color not in colors: colors.append(color)
        tree.insert(color, bbox)

        # overlaps
        boxes = tree.intersect(bbox)
        for box in boxes:
            newBoxes = subtract( bbox, box.rect )
            tree.nodes.remove(box)
            for newBox in newBoxes:
                tree.insert(box.item, newBox)


for color in colors:
    x = sum( size(x.rect) for x in tree.nodes if x.item == color)
    print(color + " " + str(x))