import random

def main(args: list[str]) -> int:
    # How many names are we going to generate?
    n: int = int(input('How many names should be generated? '))

    # Read the first names
    first_names: list[tuple[str, float]] = []
    with open('first-names.csv', 'r') as first_file:
        # Find the total proportion from the last line
        lines: list[str] = first_file.readlines() # Only call this once
        line: str = lines[-1] # last line in the file
        total_freq: float = float(line.split(',')[0])

        for line in lines[1:-1]:
            parts: list[str] = line.split(',')
            name: str = parts[1].capitalize()
            freq: float = float(parts[0])/total_freq
            first_names.append((name, freq))
            #print(first_names)

    # Read the last names
    last_names: list[tuple[str, float]] = []
    with open('last-names.csv', 'r') as last_file:
        # Find the total proportion/100k from the last line
        lines: list[str] = last_file.readlines() # Only call this once
        line: str = lines[-1] # last line in the file
        total_freq: float = float(line.split(',')[0])
        #print(total_freq)
        for line in lines[1:-1]:
            parts: list[str] = line.split(',')
            name: str = parts[1].capitalize()
            freq: float = float(parts[0])/total_freq
            last_names.append((name, freq))
        #print(last_names[:10])
    
    # Generate the names and store them in a list
    namelist: list[str] = []
    for i in range(n):
        # First name
        x: float = random.random() # 0 <= x < 1
        j: int = 0
        while j < len(first_names) and first_names[j][1] < x: # (name, freq)[1] -> freq
            j = j+1
        first: str = first_names[j-1][0] # (name, freq)[0] -> name
        #print(x, j, first)

        # Last name
        x = random.random() # 0 <= x < 1
        j = 0
        while j < len(last_names) and last_names[j][1] < x: # (name, freq)[1] -> freq
            j = j+1
        last: str = last_names[j-1][0] # (name, freq)[0] -> name
        #print(x, j, last)

        namelist.append(last + ',' + first)
    #print(namelist)

    # Write the names to an output file
    with open('names.csv', 'w') as outfile:
        # Write column headers
        outfile.write('lastname,firstname\n')
        for name in namelist:
            outfile.write(name + '\n')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))