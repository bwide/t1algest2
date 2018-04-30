import sys
sys.setrecursionlimit(10000)
from pyqtree import Index

path = sys.argv[1]

def size(bbox):
    return (bbox[2]-bbox[0])*(bbox[3]-bbox[1])

# def subtract(box1, box2):


colors = []

with open(path) as file:
    elements = int(file.readline())
    tree = Index(bbox=(0,0,50000,50000))
    for line in file:
        line = line.split(' ')

        bbox = [int(x) for x in line[:4]]
        color = line[4].strip('\n')

        if color not in colors: colors.append(color)
        # bbox = ( x0, y0, x1, y1 )

        # overlaps
        # boxes = tree.intersect(bbox)
        # for box in boxes:
        #     tree.remove(color, box)

            
        tree.insert(color, bbox)

for color in colors:
    x = sum( size(x.rect) for x in tree.nodes if x.item == color)
    print(color + " " + str(x))