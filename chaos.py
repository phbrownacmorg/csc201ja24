def main(args: list[str]) -> int:
    print('This program illustrates a chaotic function.')
    x: float = float(input('Please enter a number between 0 and 1: '))
    print('{0:>2} {1:>12}'.format('i', 'x'))
    print('-' * 15)
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print('{0:2} {1:12.6f}'.format(i, x))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))