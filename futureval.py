# Program to calculate the future value of an investment
# with a fixed rate of reurn (interest rate).
# (It also works for a loan table, running in reverse.)

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

def main(args: list[str]) -> int:
    P, rate, periods = read_parameters()
    # Echo back the parameters
    print('Investing $', P, 'at', rate, '% for', periods, 'compounding periods:')

    values = calc_futureval(P, rate/100, periods)
    print_table(values)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))