from accumulator import sum_average

def process_list(numlist: list[float]) -> None:
    print('The list of numbers is ', numlist)
    if len(numlist) > 0:
        total, avg = sum_average(numlist)
        print('Sum of', len(numlist), 'numbers =', total,
              " Average =", avg)

def nested_input() -> None:
    """Reads a list of numbers, allowing more than one per line of input.  Uses
    an exception as a "sentinel" to exit the loop."""
    numlist: list[float] = []
    try:
        while True:
            response: str = input('Please enter one or more numbers,' \
                                  + ' or anything non-numeric to exit: ')
            items: list[str] = response.split()
            if len(items) == 0: # Empty response
                raise ValueError
            for item in items:
                numlist.append(float(item))
    except ValueError:
        process_list(numlist)

def exception_sentinel() -> None:
    """Reads a list of numbers using an exception as the "sentinel" to
    exit the loop."""
    numlist: list[float] = []
    try:
        while True:
            numlist.append(float(input('Please enter a number, or anything else to quit: ')))
    except ValueError:
        process_list(numlist)

def empty_sentinel() -> None:
    """Reads a list of numbers using the empty string as a sentinel value to
    exit the loop."""
    numlist: list[float] = []
    response: str = input('Please enter a number, or just hit Enter to quit: ')
    while response != '':
        numlist.append(float(response))
        response: str = input('Please enter a number, or just hit Enter to quit: ')
    process_list(numlist)

def negative_sentinel() -> None:
    """Reads a list of numbers using a sentinel value to exit the loop.
    The sentinel here is a negative number."""
    numlist: list[float] = []
    num = float(input('Please enter a number, or a negative number to quit: '))
    while num > 0:
        numlist.append(num)
        num = float(input('Please enter a number, or a negative number to quit: '))
    process_list(numlist)

def interactive_loop() -> None:
    """Reads a list of numbers using an interactive loop.  The user
    has to agree explicitly to continue each time."""
    numlist: list[float] = []
    response: str = 'Y'
    while len(response) > 0 and response[0] in 'Yy':
        numlist.append(float(input('Please enter a number: ')))
        response = input('Would you like to enter another number? (Y/N) ')
    process_list(numlist)

def main(args: list[str]) -> int:
    #interactive_loop()
    #negative_sentinel()
    #empty_sentinel()
    #exception_sentinel()
    nested_input()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))