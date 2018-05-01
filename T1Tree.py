import sys
sys.setrecursionlimit(10000)
from pyqtree import Index
from rect import Rectangle

path = sys.argv[1]

def size(bbox):
    x1, y1, x2, y2 = bbox
    return (x2-x1)*(y2-y1)

colors = []

with open(path) as file:
    elements = int(file.readline())
    tree = Index(bbox=(0,0,50000,50000), max_depth=10000, max_items=200000 )
    for line in file:
        line = line.split(' ')
        x1, y1, x2, y2 = [int(x) for x in line[:4]]
        bbox = (x1, y1, x2, y2)
        newRect = Rectangle( x1, y1, x2, y2 )
        color = line[4].strip('\n')

        if color not in colors: colors.append(color)

        # overlaps
        boxes = tree.intersect(bbox)
        for box in boxes:
            x1, y1, x2, y2 = box.rect
            oldRect = Rectangle( x1, y1, x2, y2 )
            tree.remove(box.item, box.rect)
            for newBox in (oldRect - newRect):
                newbbox = ( newBox.x1, newBox.y1, newBox.x2, newBox.y2 )
                tree.insert(box.item, newbbox)

        tree.insert(color, bbox)


for color in colors:
    x = sum( size(x.rect) for x in tree.nodes if x.item == color)
    print(color + ": " + str(x))