import sys
sys.setrecursionlimit(10000)
from pyqtree import Index
from rect import Rectangle
import time

path = sys.argv[1]

def size(bbox):
    x1, y1, x2, y2 = bbox
    return (x2-x1)*(y2-y1)

colors = []

with open(path) as file:
    elements = int(file.readline())

    start = time.time()

    tree = Index(bbox=(0,0,50000,50000), max_depth=10000, max_items=elements*4 )
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

output = open("result", "a")
for color in colors:
    x = sum( size(x.rect) for x in tree.nodes if x.item == color)
    output.write( color + ": " + str(x) + '\n')
    
output.write('\n')
runtime = time.time() - start

minutes = runtime/60
seconds = runtime%60

output.write(path + ": " + str(round(minutes)) + "m " + str(seconds) + "s" + '\n ------ \n')
output.close()