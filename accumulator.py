def main(args: list[str]) -> int:
    # Get a list of numbers from the user, using the acumulator pattern (#1)
    list_size: int = int(input('How many numbers do you want to enter? '))
    numlist: list[float] = [] # Accumulator variable
    for i in range(list_size): # Loop
         # Accumulate another number into the list each time through the loop
        numlist.append(float(input('Please enter a number for the list: ')))
    print('The list of numbers is ', numlist)

    # Find the sum and average of the list, using the accumulator pattern
    total: float = 0    # Accumulator variable #1
    count: int = 0      # Accumulator variable #2
    for num in numlist: # Loop.  
        # Each time through, NUM has the value of the next number in the list.
        # Update accumulator variable #1
        total = total + num
        # Update accumulator variable #2
        count = count + 1
    # Print the sum and average of numlist
    print('Sum of', count, 'numbers =', total, " Average =", (total/count))

    # Find the factorial of count, using the accumulator pattern
    product: int = 1 # Accumulator variable
    for i in range(1, count+1): # Could equally be range(count, 0, -1)
        product = product * i
    print(str(count) + "! = " + str(product))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))