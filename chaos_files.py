import sys 

def main(args: list[str]) -> int:
    print('This program illustrates a chaotic function.')
    try:
        with open('chaos-seeds.csv', 'r') as infile:
            for line in infile.readlines():
                parts: list[str] = line.split(',')

                try:
                    # Get x
                    x: float = float(parts[0])
                    # Clamp x to the interval (0, 1)
                    x = max(sys.float_info.min, min(1.0 - sys.float_info.epsilon, x))
                    print('Seed = ', x)
                except ValueError as e:
                    print('x is not a number between 0 and 1.')
                    continue

                # Get n
                n: int = 10
                try:
                    n = int(parts[1])
                except ValueError as e:
                    print('n is not an integer.')
                    continue
                # Ensure that n >= 1
                n = max(1, n)

                # Run the calculation
                print('{0:>2} {1:>12}'.format('i', 'x'))
                print('-' * 15)
                for i in range(n):
                    x = 3.9 * x * (1 - x)
                    print('{0:2} {1:12.6f}'.format(i+1, x))
                print()
    except OSError as e:
        print(e)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))