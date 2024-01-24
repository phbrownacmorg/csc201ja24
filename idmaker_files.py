# Make a Converse-style userid out of a name

def read_names(filename: str) -> list[list[str]]:
    namelist: list[list[str]] = []
    with open(filename, 'r') as infile:
        for line in infile.readlines()[1:]: # Skip the column names
            nameparts: list[str] = line.split(',')
            namelist.append(nameparts)
    return namelist

def simplify_name(name: str) -> str:
    # Remove characters from the name that we don't want in the result
    unwanted_chars = " ',."
    for c in unwanted_chars:
        name = name.replace(c, '')

    # Handle (some) Unicode characters
    to_replace = "\u00e0\u00e1\u00e2\u00e3\u00e4\u00e5\u00e7\u00e8\u00e9\u00ea\u00eb" \
            + "\u00ec\u00ed\u00ee\u00ef\u00f1\u00f2\u00f3\u00f4\u00f5\u00f6\u00f8" \
            + "\u00f9\u00fa\u00fb\u00fc\u00fd\u00ff"
    replace_with = "aaaaaaceeee" \
            + "iiiinoooooo" \
            + "uuuuyy"
    for i in range(len(to_replace)):
        name = name.replace(to_replace[i], replace_with[i])
    return name

def make_initials(namestr: str) -> str:
    """Takes a NAMESTR containing one or more names, separated by white space,
    and returns a string containing the initial(s) of those name(s).  The result
    does not contain more than two initials."""
    names = namestr.split()

    # Make the initials, so we handle the case of someone with no middle name (or many)
    initials = ''
    for i in range(min(2, len(names))):
        initials = initials + names[i][0]
    return initials

def make_userids(namelist: list[list[str]]) -> list[list[str]]:
    idlist: list[list[str]] = []

    for name in namelist:
        lastname = simplify_name(name[0])
        # Assumes people have at least two names
        initials = make_initials(name[1])

        # Blithely assume we have no one else with the same first
        # and middle initials and last name
        userid = (initials + lastname + '001').lower()
        
        idlist.append([name[0], name[1].strip(), userid])
    #print(idlist)

    return idlist

def write_userids(idlist: list[list[str]], filename) -> None:
    with open(filename, 'w') as outfile:
        # Column headers
        outfile.write('lastname,firstname,userid\n')
        # Write the data
        for person in idlist:
            outfile.write(','.join(person) + '\n')

def main(args: list[str]) -> int:
    namelist: list[list[str]] = read_names('names.csv')
    idlist: list[list[str]] = make_userids(namelist)
    write_userids(idlist, 'userids.csv')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))