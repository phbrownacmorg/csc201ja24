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

def calc_futureval(P: float, rate: float, periods: int) -> list[float]:
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

def find_tick_value(maxVal: float) -> int:
    """Given a maximum value, find a tick value that is (1) round, and (2) gives
    5-15 tick marks going up to maxVal."""
    intlog = math.floor(math.log10(maxVal))
    tick = 10 ** intlog
    # tick is the biggest power of 10 <= maxVal
    # At this point, I know 1 <= (maxVal/tick) < 10
    if (maxVal / tick) < 2.5:
        tick = tick / 5 # tick is now 20, 200, 2000, etc.
        # 5 < (tick / maxVal) < 12.5
    elif (maxVal/tick) < 5: # and maxVal / tick >= 2.5
        tick = tick / 2
        # tick is now half the power of 10 (50, 500, 5000, etc.)
        # 5 <= (maxVal/tick) < 10
    return tick
    
def drawAxis(w: GraphWin, outerEnd: Point) -> None:
    axis: Line = Line(Point(0,0), outerEnd)
    axis.setArrow('last')
    axis.draw(w)

def graph(values: list[float]) -> None:
    # Find the range of values
    Xmax: int = len(values)
    Ymax: float = max(values)
    tick_spacing: int = find_tick_value(Ymax)
    Ymax = math.ceil(Ymax / tick_spacing) * tick_spacing # integer value, float type
    # Using round instead of // because Ymax could be a little smaller than it's supposed to be
    num_ticks: int = round(Ymax / tick_spacing) 
    #print(max(values), tick_spacing, Ymax, num_ticks)

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
    for i in range(num_ticks+1):
        y: int = i * tick_spacing
        tick = Line(Point(0, y), Point(-(margin/10) * Xmax, y))
        tick.draw(win)
        label = Text(Point(-(0.5 * margin) * Xmax, y), '${:,.0f}'.format(y))
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