def read_phonebook(filename: str, default_filename: str) -> dict[str, str]:
    phonebook: dict[str, str] = {}
    if filename == '':
        filename = default_filename
    with open(filename, 'r') as f:
        for line in f.readlines()[1:]: # Ignore the field names
            parts = line.split(',')
            name = parts[0].strip()
            number = parts[1].strip()
            phonebook[name] = number
    return phonebook

def write_phonebook(phonebook: dict[str, str], 
                    filename: str, default_filename: str) -> None:
    if filename == '':
        filename = default_filename
    with open(filename, 'w') as f:
        # Column headers
        f.write('name,number\n')
        for name in iter(phonebook):
            f.write(name + ',' + phonebook[name] + '\n')

def normalize_name(name: str) -> str:
    """Takes a NAME and returns it as "Firstname Lastname", regardless of how
    it was capitalized, whether it was entered last name first, and whether
    a middle name was included or not.  If only one name is entered, it is
    assumed to be the last name.  This function does not attempt to be smart
    about capitalizations (such as 'von Richthofen') or spaces within names."""
    name = name.title() # So a query with odd capitalization still finds the entry
    # Try to standardize different forms of the name
    if ',' in name: # Last name first
        nameparts = name.split(',') # Last name first
        lastname = nameparts[0]
        nameparts = nameparts[1].split() # Split on white space
        firstname = nameparts[0] + ' '
    else: # No comma, first name first
        nameparts = name.split()
        lastname = nameparts[-1] # Always there
        if len(nameparts) > 1: # More than one name
            firstname = nameparts[0] + ' '
        else:
            firstname = ''
    return firstname + lastname

def add_entry(phonebook: dict[str, str]) -> None:
    """Get a new phonebook entry from the user, and add it to the phonebook."""
    print('Adding')
    name: str = normalize_name(input("Please enter the person's name: "))
    number: str = input("Please enter the person's phone number: ")
    phonebook[name] = number

def lookup_entry(phonebook: dict[str, str]) -> None:
    print('Looking up')
    name: str = normalize_name(input("Please enter the person's name: "))
    number: str | None = phonebook.get(name) # Use the safe version
    if number is None:
        print('The phone book does not have an entry for "{}".'.format(name))
    else:
        print('The number for {} is {}.'.format(name, number))


def main(args: list[str]) -> int:
    default_filename = 'phonebook.csv'
    filename: str = input('Please enter a filename to read from '
                     + '(default {}): '.format(default_filename))
    phonebook: dict[str, str] = read_phonebook(filename, default_filename)
    print(phonebook)
    
    op = input('Would you like to add an entry (A), '
               + 'look up an entry (L), or quit (Q)? (A/L/Q) ').upper()
    while len(op) > 0 and op[0] in 'AL': # Make it easy to quit
        if op[0] == 'A':
            add_entry(phonebook)
        elif op[0] == 'L':
            lookup_entry(phonebook)
        print(phonebook)
        op = input('Would you like to add an entry (A), '
                    + 'look up an entry (L), or quit (Q)? (A/L/Q) ').upper()
    filename = input('Please enter a filename to write to '
                     + '(default {}): '.format(default_filename))
    write_phonebook(phonebook, filename, default_filename)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))