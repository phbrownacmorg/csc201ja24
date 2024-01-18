def article(word: str) -> str:
    """Find the proper indefinite article for a given WORD."""
    result = 'a'
    if word[0].lower() in 'aeiou':
        result = 'an'
    return result

def printVerse(animals: str, noise: str) -> None:
    artic: str = article(noise)
    print('Old MacDonald had a farm, E-I-E-I-O,')
    print('And on that farm he had some {}, E-I-E-I-O,'.format(animals))
    print('With {1} {0}, {0} here and {1} {0}, {0} there,'.format(noise, artic))
    print('Here {1} {0}, there {1} {0}, everywhere {1} {0}, {0},'.format(noise, artic))
    print('Old MacDonald had a farm, E-I-E-I-O!\n')

def main(args: list[str]) -> int:
    printVerse('cows', 'moo')
    printVerse('geese', 'honk')
    printVerse('pigs', 'oink')
    printVerse('chickens', 'cluck')
    printVerse('dogs', 'bark')
    printVerse('monkey', 'ooh')
    printVerse('goat', 'maa')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))