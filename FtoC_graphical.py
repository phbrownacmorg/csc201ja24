from graphics import *

def main(args: list[str]) -> int:
    w: GraphWin = GraphWin('Graphics window', 400, 100)
    # Rearrange the coordinate system to be easier to think about.
    # X increases to the right, Y increases up.  The origin is in
    # the center, and the absolute value of any coordinate tells you
    # proportionally how close it is to the edge.
    # The layout of the picture no longer depends on the size of
    # the window (it will scale to any size).
    w.setCoords(-1, -1, 1, 1)

    instructions: Text = Text(Point(0, 0.5), 'Specify a temperature and click to convert to Celsius:')
    instructions.draw(w)

    degF_entry: Entry = Entry(Point(0, 0), 6)
    degF_entry.draw(w)

    # Wait for the mouse click to convert
    w.getMouse()

    # Do the conversion and display the results
    # Get the degrees F
    degF: float = float(degF_entry.getText())
    # Convert to degrees C
    degC: float = (degF - 32) * 5/9
    # Display the result
    label: Text = Text(Point(0, -0.5), 
                       str(round(degF, 1)) + '\u00b0 F = ' +
                       str(round(degC, 1)) + '\u00b0 C')
    label.draw(w)

    # DRAW STUFF HERE


    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))