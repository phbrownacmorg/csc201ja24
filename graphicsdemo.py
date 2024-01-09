from graphics import *

def main(args: list[str]) -> int:
    w = GraphWin('Graphics window', 500, 500)
    # Rearrange the coordinate system to be easier to think about.
    # X increases to the right, Y increases up.  The origin is in
    # the center, and the absolute value of any coordinate tells you
    # proportionally how close it is to the edge.
    # The layout of the picture no longer depends on the size of
    # the window (it will scale to any size).
    w.setCoords(-1, -1, 1, 1)

    p = Point(0, 0)
    p.draw(w)

    p1 = Point(-0.75, 0)
    p1.draw(w)

    p2 = Point(0, -0.75)
    p2.draw(w)

    line = Line(p1, p)
    line.setOutline('blue')
    line.draw(w)

    c = Circle(p, 0.625)
    c.setFill('medium spring green')
    c.draw(w)

    rect = Rectangle(p, Point(0.5, -0.5))
    rect.setFill('pink')
    rect.draw(w)

    oval = Oval(p, Point(0.5, 0.125))
    oval.setFill('DarkSeaGreen1')
    oval.draw(w)

    poly = Polygon(p, p2, Point(-0.75, -0.375))
    poly.setFill('gray')
    poly.draw(w)

    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))