from datetime import date, timedelta

def easter(year: int) -> date:
    if year < 1982 or year > 2048:
        raise ValueError('Year must be in the range 1982-2048, inclusive.')

    a: int = year % 19
    b: int = year % 4 # Leap year or not
    c: int = year % 7 # day of week (kind of)
    d: int = (19*a + 24) % 30
    e: int = (2*b + 4*c + 6*d + 5) % 7
    result: date = date(year, 3, 22) + timedelta(d) + timedelta(e)
    return result

def main(args: list[str]) -> int:
    year: int = int(input('Please enter a year in the range 1982-2048,'
                          + ' inclusive: '))
    print('Easter of ', year, end=' ')
    print('is', easter(year))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))