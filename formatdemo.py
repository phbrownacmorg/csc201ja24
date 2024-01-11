def main(args: list[str]) -> int:
    # Phone numbers
    print('{0}-{1}-{2}'.format('864', '596', '9000'))
    print('{0}.{1}.{2}'.format('864', '596', '9000'))
    print('({0}) {1}-{2}'.format('864', '596', '9000'))
    print('1-{0}-{1}-{2}'.format('864', '596', '9000'))
    print('+1 {0}-{1}-{2}'.format('864', '596', '9000'))

    # Social Security number, using slicing to extract the parts
    print('{0}-{1}-{2}'.format('123456789'[:3], '123456789'[3:5], '123456789'[-4:]))

    # Dates
    print('{0}-{1:02d}-{2:02d}'.format(2024, 1, 10)) # ISO 8609
    print('{1}/{2}/{0}'.format(2024, 1, 10)) # American
    print('{2}/{1}/{0}'.format(2024, 1, 10)) # British
    print('{2}.{1}.{0}'.format(2024, 1, 10))
    print('{1}.{2}.{0}'.format(2024, 1, 10))
    print('{1:02}-{2:02}-{0:2d}'.format(2024 % 100, 1, 10))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))