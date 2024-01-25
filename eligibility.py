def eligibleSenate(age: int, yearsCitizen: int) -> bool:
    """Senators must be at least 30, and have been a U.S. 
    citizen for at least 9 years."""
    return True

def eligibleHR(age: int, yearsCitizen: int) -> bool:
    """Representatives must be at least 25, and have been a 
    U.S. citizen for at least 7 years."""
    return age >= 25 and yearsCitizen >= 7

def main(args: list[str]) -> int:
    age: int = int(input("Please enter a person's age: "))
    years_a_citizen: int = int(input('How long has this person been a U.S. citizen? '))

    print('A person aged', age, 'who has been a U.S. citizen for',
          years_a_citizen, 'years is', end='\n\t')
    if not eligibleHR(age, years_a_citizen):
        print('NOT', end=' ')
    print('eligible to serve in the U.S. House of Representatives.')

    # Check eligibility for Senate and print something appropriate

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))