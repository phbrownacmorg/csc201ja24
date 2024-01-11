from graphics import *
import math

def main(args: list[str]) -> int:
    w: GraphWin = GraphWin('Graphics window', 800, 800)
    # Rearrange the coordinate system to be easier to think about.
    # X increases to the right, Y increases up.  The origin is in
    # the center, and the absolute value of any coordinate tells you
    # proportionally how close it is to the edge.
    # The layout of the picture no longer depends on the size of
    # the window (it will scale to any size).
    w.setCoords(-1, -1, 1, 1)

    p1: Point = w.getMouse()
    p1.draw(w)
    label = Text(Point(0, .95), 'Point 1: ({0:.4f}, {1:.4f})'.format(
        p1.getX(), p1.getY()))
    label.draw(w)

    p2: Point = w.getMouse()
    p2.draw(w)
    label = Text(Point(0, .9), 'Point 2: ({0:.4f}, {1:.4f})'.format(
        p2.getX(), p2.getY()))
    label.draw(w)

    line: Line = Line(p1, p2)
    line.draw(w)
    length: float = math.sqrt((p1.getX() - p2.getX())**2 +
                              (p1.getY() - p2.getY())**2)
    label = Text(Point(0, 0.85), 
                 'Line length: {0:.4f}'.format(length))
    label.draw(w)

    # DRAW STUFF HERE


    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))