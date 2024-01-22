from graphics import *
import math
from typing import cast
from button import make_button, inside

def drawAnimal(animal: list[GraphicsObject], w: GraphWin) -> None:
    for part in animal:
        part.draw(w)

def getCenter(animal: list[GraphicsObject]) -> Point:
    return cast(Circle, animal[0]).getCenter()

def moveAnimalTo(animal: list[GraphicsObject], destination: Point) -> None:
    currentLoc: Point = getCenter(animal)
    dx: float = destination.getX() - currentLoc.getX()
    dy: float = destination.getY() - currentLoc.getY()
    for part in animal:
        part.move(dx, dy)

def makeEyes(radius: float, color: str) -> list[GraphicsObject]:
    eyeList: list[GraphicsObject] = []
    for x_sign in [-1, 1]:
        eye: Oval = Oval(Point(x_sign * 0.05 * radius, 0), Point(x_sign * 0.6 * radius, 0.7 * radius))
        eye.setFill(color)
        eyeList.append(eye)
    return eyeList

def makeMouseEars(radius: float, color: str) -> list[GraphicsObject]:
    earList: list[GraphicsObject] = []
    angle = math.radians(55)
    ear_radius = 0.6 * radius
    for x_sign in [-1, 1]:
        ear: Circle = Circle(Point(1.3 * radius * math.cos(angle) * x_sign,
                                   1.3 * radius * math.sin(angle)), ear_radius)
        ear.setOutline(color)
        ear.setFill(color)
        earList.append(ear)
    return earList

def makeCatEars(radius: float, color: str) -> list[GraphicsObject]:
    earList: list[GraphicsObject] = []
    central_angle = math.radians(55)
    side_angle = math.radians(25)
    tip_radius = 1.8 * radius
    for x_sign in [-1, 1]:
        tip = Point(tip_radius * math.cos(central_angle) * x_sign,
                    tip_radius * math.sin(central_angle))
        top = Point(radius * math.cos(central_angle + side_angle) * x_sign,
                    radius * math.sin(central_angle + side_angle))
        bottom = Point(radius * math.cos(central_angle - side_angle) * x_sign,
                       radius * math.sin(central_angle - side_angle))
        ear = Polygon(tip, top, bottom)
        ear.setFill(color)
        ear.setOutline(color)
        earList.append(ear)
    return earList

def makeMouth(radius: float) -> list[GraphicsObject]:
    lines: list[GraphicsObject] = []
    angle = math.radians(-55)
    length = 0.6
    for x_sign in [-1, 1]:
        line = Line(Point(0, -0.3 * radius), 
                    Point(length * radius * math.cos(angle) * x_sign,
                          length * radius * math.sin(angle)))
        lines.append(line)
    return lines

def makeNose(radius: float, color: str) -> Polygon:
    size = 0.3
    nose = Polygon(Point(0, -size * radius),
                   Point((-size/2) * radius, 0),
                   Point((size/2) * radius, 0))
    nose.setFill(color)
    return nose

def makeWhiskers(radius: float) -> list[GraphicsObject]:
    whiskerList: list[GraphicsObject] = []
    inner_r = 0.7
    outer_r = 1.7
    angle = math.radians(10)
    for x_sign in [1, -1]:
        for i in [-1, 0, 1]:
            whisker = Line(Point(x_sign * inner_r * radius * math.cos(i * angle),
                                 inner_r * radius * math.sin(i * angle)),
                           Point(x_sign * outer_r * radius * math.cos(i * angle),
                                 outer_r * radius * math.sin(i * angle)))
            whiskerList.append(whisker)
    return whiskerList

def makeHead(radius: float, color: str) -> Circle:
    head = Circle(Point(0, 0), radius)
    head.setFill(color)
    head.setOutline(color)
    return head

def makeMouse(radius: float) -> list[GraphicsObject]:
    result: list[GraphicsObject] = [makeHead(radius, 'gray')]
    result.extend(makeMouseEars(radius, 'gray'))
    result.extend(makeEyes(radius, 'black'))
    result.extend(makeMouth(radius))
    result.append(makeNose(radius, 'black'))
    result.extend(makeWhiskers(radius))
    return result

def makeCat(radius: float) -> list[GraphicsObject]:
    result: list[GraphicsObject] = [makeHead(radius, 'orange')]
    result.extend(makeCatEars(radius, 'orange'))
    result.extend(makeEyes(radius, 'green'))
    result.extend(makeMouth(radius))
    result.append(makeNose(radius, 'black'))
    result.extend(makeWhiskers(radius))
    return result

def caught(predator: list[GraphicsObject], prey: list[GraphicsObject]) -> bool:
    """Returns True if the distance between predator and prey is less than the
    radius of the predator (that is, the predator has caught the prey)."""
    predatorPt = getCenter(predator)
    preyPt = getCenter(prey)
    distance = math.sqrt((predatorPt.getX() - preyPt.getX())**2 + 
                         (predatorPt.getY() - preyPt.getY())**2)
    return distance < cast(Circle, predator[0]).getRadius()


def main(args: list[str]) -> int:
    w: GraphWin = GraphWin('Graphics window', 800, 800)
    # Rearrange the coordinate system to be easier to think about.
    # X increases to the right, Y increases up.  The origin is in
    # the center, and the absolute value of any coordinate tells you
    # proportionally how close it is to the edge.
    # The layout of the picture no longer depends on the size of
    # the window (it will scale to any size).
    w.setCoords(-1, -1, 1, 1)

    quit_button = make_button(w, Point(-1, 1), Point(-.8, .8),
                            'Quit')

    mouse: list[GraphicsObject] = makeMouse(0.05)
    drawAnimal(mouse, w)
    cat: list[GraphicsObject] = makeCat(0.2)
    moveAnimalTo(cat, Point(2, 0))
    drawAnimal(cat, w)

    # DRAW STUFF HERE
    # Chase the mouse for 5 mouse clicks
    distance = 2
    click = w.getMouse()
    while not inside(quit_button, click) and not caught(cat, mouse):
        mousePt = getCenter(mouse)
        moveAnimalTo(mouse, click)
        moveAnimalTo(cat, mousePt)
        click = w.getMouse() # MUST update the variable used in the loop condition

    # Force the window to stay open until we click
    #w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))