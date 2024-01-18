# Program to take a year from the user and print out whether
# the year is a leap year.

from datetime import datetime

def is_leap_year(year: int) -> bool:
    """Returns a Boolean indicating whether the given YEAR is a leap year,
    using the rules for the Gregorian calendar."""
    # Gregorian leap-year rules:
    #   - If a year is evenly divisible by 400, it's a leap year.
    #   - If it's evenly divisible by 100 but not by 400, it's not a leap year.
    #   - If it's evenly divisible by 4 but not by 100, it's a leap year.
    #   - If it's not evenly divisible by 4, it's not a leap year.
    leap: bool = False # True basically 3/4 of the time
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0 and year % 400 != 0:
        leap = False
    elif year % 400 == 0:
        leap = True
    return leap

def past_present_future(year: int) -> str:
    """Returns the proper form of the verb "to be" for the given YEAR.  That is,
    for a year in the past it returns 'was'; for the current year it returns
    'is'; and for a year in the future it returns 'will be'."""
    now: datetime = datetime.now()
    result = 'is'
    if year < now.year: # Year is in the past
        result = 'was'
    elif year > now.year: # Year is in the future
        result = 'will be'
    return result

def main(args: list[str]) -> int:
    year: int = int(input('Please enter a Gregorian year (i.e., year > 1581): '))
    print('The year', year, past_present_future(year), end=' ') # FIX verb tense
    if not is_leap_year(year):
        print('NOT', end= ' ')
    print('a leap year.')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))