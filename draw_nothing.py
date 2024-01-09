from graphics import *

def main(args: list[str]) -> int:
    w = GraphWin('Graphics window', 800, 800)

    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))