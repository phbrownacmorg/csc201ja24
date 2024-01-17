def printVerse(animals: str, noise: str) -> None:
    print('Old MacDonald had a farm, E-I-E-I-O,')
    print('And on that farm he had some {}, E-I-E-I-O,'.format(animals))
    print('With a {0}, {0} here and a {0}, {0} there,'.format(noise))
    print('Here a {0}, there a {0}, everywhere a {0}, {0},'.format(noise))
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