# Program to convert Fahrenheit temperatures to Celsius

def main(args: list[str]) -> int:
    # Read a temperature from the keyboard
    degF: float = float(input('Please enter a Fahrenheit temperature: '))

    # Bogus processing step
    degC: float = (degF - 32) * 5/9

    # Output
    print(degF, 'degrees Fahrenheit =', degC, 'degrees Celsius')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))