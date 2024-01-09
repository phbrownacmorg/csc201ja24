from graphics import *

def main(args: list[str]) -> int:
    w = GraphWin('Graphics window', 800, 800)

    p = Point(400, 400)
    p.draw(w)

    p1 = Point(100, 400)
    p1.draw(w)

    p2 = Point(400, 100)
    p2.draw(w)

    line = Line(p1, p)
    line.setOutline('blue')
    line.draw(w)

    c = Circle(p, 250)
    c.setFill('medium spring green')
    c.draw(w)

    rect = Rectangle(p, Point(600, 200))
    rect.setFill('pink')
    rect.draw(w)

    oval = Oval(p, Point(600, 450))
    oval.setFill('DarkSeaGreen1')
    oval.draw(w)

    poly = Polygon(p, p2, Point(100, 250))
    poly.setFill('gray')
    poly.draw(w)

    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))