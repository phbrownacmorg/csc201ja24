from graphics import *

def main(args: list[str]) -> int:
    w: GraphWin = GraphWin('Graphics window', 300, 120)
    # Rearrange the coordinate system to be easier to think about.
    # X increases to the right, Y increases up.  The origin is in
    # the center, and the absolute value of any coordinate tells you
    # proportionally how close it is to the edge.
    # The layout of the picture no longer depends on the size of
    # the window (it will scale to any size).
    w.setCoords(-1, -1, 1, 1)

    instructions: Text = Text(Point(0, 0.5), 
                              'Put a color name (or hexadecimal color\n'
                              + 'specification) in the blank, and click\n'
                              + 'to set the background color of the window.')
    instructions.draw(w)

    print(color_rgb(0, 255, 255))

    entry: Entry = Entry(Point(0, -0.5), 20)
    entry.setFill('white')
    entry.draw(w)

    w.getMouse()
    w.setBackground(entry.getText())

    # DRAW STUFF HERE


    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))