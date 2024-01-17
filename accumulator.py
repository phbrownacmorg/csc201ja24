def read_numbers() -> list[float]:
    """Get a list of numbers from the user, using the accumulator pattern."""
    list_size: int = int(input('How many numbers do you want to enter? '))
    numlist: list[float] = [] # Accumulator variable
    for i in range(list_size): # Loop
         # Accumulate another number into the list each time through the loop
        numlist.append(float(input('Please enter a number for the list: ')))
    return numlist

def sum_average(numlist: list[float]) -> tuple[float, float]:
    """Takes a list of numbers NUMLIST and returns the sum and average of the
    list as a tuple.  Uses the accumulator pattern."""
    total: float = 0    # Accumulator variable #1
    count: int = 0      # Accumulator variable #2
    for num in numlist: # Loop.  
        # Each time through, NUM has the value of the next number in the list.
        # Update accumulator variable #1
        total = total + num
        # Update accumulator variable #2
        count = count + 1
    return total, total/count

def fact(n: int) -> int:
    """Find the factorial of a positive integer using the accumulator pattern."""
    product: int = 1
    # Accumulator variable
    for i in range(1, n+1): # Could equally be range(n, 0, -1)
        product = product * i
    return product

def main(args: list[str]) -> int:
    numlist: list[float] = read_numbers()
    print('The list of numbers is ', numlist)

    total, avg = sum_average(numlist)
    print('Sum of', len(numlist), 'numbers =', total, " Average =", avg)

    # Find the factorial of the length of the list
    count = len(numlist)
    print(str(count) + "! = " + str(fact(count)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))