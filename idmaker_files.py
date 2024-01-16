# Make a Converse-style userid out of a name

def main(args: list[str]) -> int:
    namelist: list[list[str]] = []
    with open('names.csv', 'r') as infile:
        for line in infile.readlines()[1:]:
            nameparts: list[str] = line.split(',')
            namelist.append(nameparts)

    idlist: list[list[str]] = []
    for name in namelist:
        lastname = name[0]

        # Assumes people have at least two names
        nameparts = name[1].split()
        #print(nameparts)

        # Make the initials, so we handle the case of someone with no middle name
        initials = ''
        for i in range(min(2, len(nameparts))):
            initials = initials + nameparts[i][0]

        # Remove characters from the last name that we don't want in the result
        unwanted_chars = " '"
        for c in unwanted_chars:
            lastname = lastname.replace(c, '')

        # Handle (some) Unicode characters
        to_replace = "\u00e0\u00e1\u00e2\u00e3\u00e4\u00e5\u00e7\u00e8\u00e9\u00ea\u00eb" \
                + "\u00ec\u00ed\u00ee\u00ef\u00f1\u00f2\u00f3\u00f4\u00f5\u00f6\u00f8" \
                + "\u00f9\u00fa\u00fb\u00fc\u00fd\u00ff"
        replace_with = "aaaaaaceeee" \
                + "iiiinoooooo" \
                + "uuuuyy"
        for i in range(len(to_replace)):
            lastname = lastname.replace(to_replace[i], replace_with[i])

        # Blithely assume we have no one else with the same first
        # and middle initials and last name
        userid = (initials + lastname + '001').lower()
        
        idlist.append([lastname, nameparts[0], userid])
    #print(idlist)
    
    with open('userids.csv', 'w') as outfile:
        # Column headers
        outfile.write('lastname,firstname,userid\n')
        # Write the data
        for person in idlist:
            outfile.write(','.join(person) + '\n')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))