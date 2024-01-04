# Program to calculate the future value of an investment
# with a fixed rate of reurn (interest rate).
# (It also works for a loan table, running in reverse.)

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

    # Loop
    for i in range(periods):
        # Find the interest
        interest: float = P * rate
        # Find the new principal = P + interest
        P = P + interest
        print(str(i+1) + '\t$' + str(round(interest, 2)) + '\t\t$' + str(round(P, 2)))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))