import math

def main(args: list[str]) -> int:
    # Read an integer from the keyboard
    numstring = ''

    num: int = int(input('Please enter an integer: '))

    numdigits: int = int(math.ceil(math.log10(num)))

    for i in range(numdigits):
        digit = chr(num % 10 + ord('0'))
        numstring = digit + numstring
        print(numstring)
        num = num // 10

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))