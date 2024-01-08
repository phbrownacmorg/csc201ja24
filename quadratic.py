def main(args: list[str]) -> int:
    # Characterize the function as a*x**2 + b*x + c = 0
    # Ask the user for a, b, and c
    print('Finding roots for a system a*x**2 + b*x + c = 0.')
    a: float = float(input("Please enter a value for a: "))
    b: float = float(input("Please enter a value for b: "))
    c: float = float(input("Please enter a value for c: "))
    print("System is", a, '*x**2 +', b, '*x +', c, '= 0')

    # find the root(s)

    # print the root(s)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))