from datetime import date

def read_temps(filename: str) -> dict[date, float]:
    temps: dict[date, float] = {}
    with open(filename, 'r') as f:
        for line in f.readlines()[1:]: # Ignore the field names
            parts = line.split(',')
            thisdate = date.fromisoformat(parts[0])
            number = float(parts[1])
            temps[thisdate] = number
    return temps

def temps_to_degdays(temps: dict[date, float]) -> dict[str, float]:
    """Constructs a dictionary mapiing days of the week to heating
    degree-days, based on the given dictionary TEMPS of daily average
    temperatures."""
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                 'Friday', 'Saturday', 'Sunday']
    degdays: dict[str, float] = {}
    for thisdate in iter(temps):
        dow = day_names[thisdate.weekday()]
        temp = temps[thisdate]
        heatingdays: float = 65 - temp
        if dow not in degdays:
            degdays[dow] = heatingdays
        else: # Already have some degree-days for this day of the week
            degdays[dow] = degdays[dow] + heatingdays
    return degdays

def main(args: list[str]) -> int:
    # Read the temperatures
    default_filename = 'temperatures.csv'
    temps: dict[date, float] = read_temps(default_filename)
    print(temps)
    degdays: dict[str, float] = temps_to_degdays(temps)
    print(degdays)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))