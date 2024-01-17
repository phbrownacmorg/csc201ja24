# Program to calculate the future value of an investment
# with a fixed rate of reurn (interest rate).
# (It also works for a loan table, running in reverse.)

from graphics import *
import math

def read_parameters() -> tuple[float, float, int]:
    # Read in the initial parameters: 
    #   - initial investment
    #   - interest rate (per period)
    #   - number of compounding periods
    P: float = float(input('Please enter a dollar value to invest: $'))
    rate: float = float(input('Please enter an interest rate per period, as a percentage: '))
    periods: int = int(input('Please enter the number of periods: '))
    return P, rate, periods

def calc_futureval(P: float, rate: float, periods: int):
    """Calculate the future value of an investment with principal P
    and interest rate RATE (as a quantity, not a percentage), over
    PERIODS compounding periods.  Returns a list of PERIODS+1 numbers,
    representing the principal at the end of each of the compounding
    periods."""
    values: list[float] = [P]
    for i in range(periods):
        interest = P * rate
        P = P + interest
        values.append(P)
    return values

def print_table(values: list[float]) -> None:

    # Print table headers
    print('{:^7}\t{:^10}\t{:^12}'.format('Period', 'Interest', 'Amount'))
    # Print first line
    print('Initial\t{:10}\t${:11.2f}'.format(' ', values[0]))
    for i in range(1, len(values)):
        print('{0:4}\t${1:9.2f}\t${2:11.2f}'.format(i, values[i]-values[i-1], values[i]))

# For later
# def find_tick_value(maxVal: float) -> int:
#     """Given a maximum value, find a tick value that is (1) round, and (2) gives
#     3-15 tick marks going up to maxVal."""
#     intlog = math.floor(math.log10(maxVal))
#     tick = 10 ** intlog # Known to be round number, fewer than 10
#     # if maxVal / tick > 3, that's my answer

def drawAxis(w: GraphWin, outerEnd: Point) -> None:
    axis: Line = Line(Point(0,0), outerEnd)
    axis.setArrow('last')
    axis.draw(w)

def graph(values: list[float]) -> None:
    # Find the range of values
    Xmax: int = len(values)
    Ymax: float = max(values)
    #tick_spacing: int = find_tick_value(Ymax)
    margin: float = .15

    # Create the window and set its coordinates
    win: GraphWin = GraphWin('Future value', 800, 800)
    win.setCoords(-margin * Xmax, -margin * Ymax,
                  (1 + margin) * Xmax, (1 + margin) * Ymax)
    
    drawAxis(win, Point((1 + (margin/2)) * Xmax, 0)) # X-axis
    drawAxis(win, Point(0, (1 + (margin/2)) * Ymax)) # Y-axis

    # Draw bars
    for i in range(len(values)):
        bar: Rectangle = Rectangle(Point(i, 0), Point(i+1, values[i]))
        bar.setFill('green') # Arbitrary; could be parameterized
        bar.draw(win)

    # Labels in X
    for i in range(len(values)):
        label = Text(Point(i + 0.5, -(margin/5) * Ymax), str(i))
        label.draw(win)

    # Labels in Y
    for i in range(len(values)):
        label = Text(Point(i + 0.5, values[i] + ((margin/5) * Ymax)), 
                     '$'+str(round(values[i])))
        label.draw(win)

    # Wait for a click so we can see it
    win.getMouse()
    win.close()

def main(args: list[str]) -> int:
    P, rate, periods = read_parameters()
    # Echo back the parameters
    print('Investing $', P, 'at', rate, '% for', periods, 'compounding periods:')

    values = calc_futureval(P, rate/100, periods)
    print_table(values)
    graph(values)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))