def main(args: list[str]) -> int:
    print('This program illustrates a chaotic function.')
    try:
        x: float = float(input('Please enter a number between 0 and 1: '))
        if not (x > 0 and x < 1):
            raise ValueError('Input is not between 0 and 1.')
    except ValueError as e:
        if e.args[0].startswith('could not convert string to float'):
            # Built-in error message is too general.  Replace it.
            print('Input must be a number between 0 and 1.')
        else:
            print(e) # Gievs me the error message put in when the exception
                     # was raised
    else:
        print('{0:>2} {1:>12}'.format('i', 'x'))
        print('-' * 15)
        i = 0
        while i < 10:
            x = 3.9 * x * (1 - x)
            print('{0:2} {1:12.6f}'.format(i, x))
            i = i + 1 # This is easy to forget!
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))