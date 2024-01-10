from graphics import *

def main(args: list[str]) -> int:
    # Read in the initial parameters: 
    #   - initial investment
    #   - interest rate (per period)
    #   - number of compounding periods
    P: float = float(input('Please enter a dollar value to invest: $'))
    rate: float = float(input('Please enter an interest rate per period, as a percentage: '))
    periods: int = int(input('Please enter the number of periods: '))

    # Echo back the parameters
    print('Investing $', P, 'at', rate, '% for', periods, 'compounding periods:')

    # Print table headers
    print('Period\tInterest\tAmount')
    # Print first line
    print('Initial\t\t\t$', P)

    # Change the interest rate from a percentage to a value
    rate = rate/100

    # Find the biggest value of P
    Pmax: float = P * ((1 + rate)**periods)
    #print(Pmax)

    w = GraphWin('Graphics window', 800, 800)

    # Reset the coordinates to fit the graph
    margin: float = 0.1
    w.setCoords(-margin*periods, -margin*Pmax, 
                (1 + margin) * periods, (1 + margin) * Pmax)

    # Draw axes
    origin: Point = Point(0, 0)
    xAxis: Line = Line(origin, Point(periods * (1 + (margin/2)), 0))
    xAxis.setArrow('last')
    xAxis.draw(w)
    yAxis: Line = Line(origin, Point(0, Pmax * (1 + (margin/2))))
    yAxis.setArrow('last')
    yAxis.draw(w)

    # Draw the bars
    for i in range(periods):
        # Find the interest
        interest: float = P * rate
        # Find the new principal = P + interest
        P = P + interest
        print(str(i+1) + '\t$' + str(round(interest, 2)) + '\t\t$' + str(round(P, 2)))

        # The bar is defined by its lower-left and upper-right corners
        bar: Rectangle = Rectangle(Point(i, 0), Point(i+1, P))
        bar.setFill('green')
        bar.draw(w)

        # Data labels
        label: Text = Text(Point(i+0.5, -0.02 * Pmax), str(i+1))
        label.draw(w)
        label: Text = Text(Point(i+0.5, P + 0.02 * Pmax), '$' + str(round(P, 2)))
        label.draw(w)

    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))