import math

def read_quadratic() -> tuple[float, float, float]:
    """Read the coefficients for a quadratic in the form
    a*x**2 + b*x + c = 0, and return them as a tuple."""
    print('Please enter coefficients for a system a*x**2 + b*x + c = 0.')
    a: float = float(input("Please enter a value for a: "))
    b: float = float(input("Please enter a value for b: "))
    c: float = float(input("Please enter a value for c: "))
    return a, b, c

def find_roots(a: float, b: float, c: float) -> tuple[float, float]:
    """Find the roots of a quadratic A*x**2 + B*x + C = 0, and return them
    as a tuple.  If there are no real roots, this returns the tuple (NaN, NaN)."""
    root1, root2 = math.nan, math.nan
    determinant: float = b**2 - 4*a*c
    #print(determinant) # for testing
    if determinant >= 0: # Don't take the square root of a negative number
        root1 = (-b + math.sqrt(determinant)) / (2*a)
        root2 = (-b - math.sqrt(determinant)) / (2*a)
    return root1, root2

def main(args: list[str]) -> int:
    # Characterize the function as a*x**2 + b*x + c = 0
    # Ask the user for a, b, and c
    a, b, c = read_quadratic()
    print("System is", a, '*x**2 +', b, '*x +', c, '= 0')

    # find the root(s)
    root1, root2 = find_roots(a, b, c)    
    # print the root(s)
    if not math.isnan(root1): # if root1 is real, so is root2
        print('The roots are', root1, 'and', root2)
    else:
        print('There are no real roots.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))