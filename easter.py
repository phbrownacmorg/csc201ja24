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

def inMarch(d: date) -> bool:
    return d.month == 3

def datesEqual(dateTuple: tuple[date, date]) -> bool:
    return dateTuple[0].month == dateTuple[1].month and \
        dateTuple[0].day == dateTuple[1].day

def datesMatch(d1: date, d2: date) -> bool:
    return d1.month == d2.month and d1.day == d2.day

def main(args: list[str]) -> int:
    year: int = int(input('Please enter a year in the range 1982-2048,'
                          + ' inclusive: '))
    print('Easter of ', year, end=' ')
    print('is', easter(year))

    # Use map to find all the dates of Easter from 1982-2048, inclusive
    easters = list(map(easter, range(1982, 2049)))

    # Filter them to find the ones in March
    march_easters = list(filter(inMarch, easters))
    for d in march_easters:
        print(d)
    print()

    # list comprehensions
    # Generate all the dates from 3/22 to 4/25, inclusive
    dates = [date(2024, 3, 22) + timedelta(i) for i in range(34)]

    # Use an "if" within the comprehension to limit to the ones in March
    march_dates = [date(2024, 3, 22) + timedelta(i) for i in range(34) if i < 10]
    for d in march_dates:
        print(d)

    print()
    pairs = [e for d in dates for e in easters if datesMatch(d, e)]
    for p in pairs:
        print(p)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))