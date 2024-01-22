# Program to convert Fahrenheit temperatures to Celsius

def main(args: list[str]) -> int:
    ABSOLUTE_ZERO = -459.67
    # Value from https://www.nbcnews.com/mach/science/what-absolute-zero-ncna936581
    # Read a temperature from the keyboard
    try:
        degF: float = float(input('Please enter a Fahrenheit temperature: '))
        if degF < ABSOLUTE_ZERO:
            raise ValueError('The temperature must be above absolute zero (-459.67\u00b0 F).')
    except ValueError as e:
        if e.args[0].startswith('The temperature must be above absolute zero'):
            print(e)
        else:
            print('Fahrenheit temperatures must be numbers.')
    else:
        # Bogus processing step
        degC: float = (degF - 32) * 5/9

        # Output
        print(degF, 'degrees Fahrenheit =', degC, 'degrees Celsius')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))