from graphics import *

def main(args: list[str]) -> int:
    w = GraphWin('Graphics window', 800, 800)
    # Rearrange the coordinate system to be easier to think about.
    # X increases to the right, Y increases up.  The origin is in
    # the center, and the absolute value of any coordinate tells you
    # proportionally how close it is to the edge.
    # The layout of the picture no longer depends on the size of
    # the window (it will scale to any size).
    w.setCoords(-1, -1, 1, 1)

    mouse = Circle(Point(0, 0), 0.05)
    mouse.setFill('gray')
    mouse.draw(w)

    # DRAW STUFF HERE
    # Chase the mouse for 5 mouse clicks
    for i in range(5):
        pt = w.getMouse()
        # Move the little gray mouse to the click
        mousePt = mouse.getCenter()
        mouse.move(pt.getX() - mousePt.getX(),
                   pt.getY() - mousePt.getY())

    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))