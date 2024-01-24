def standing(hours: int) -> str:
    result = ''
    if 0 <= hours < 24:
        result = 'freshman'
    elif hours < 56:
        result = 'sophomore'
    elif hours < 87:
        result = 'junior'
    elif hours >= 87:
        result = 'senior'
    return result

def main(args: list[str]) -> int:
    # Get a number of credit hours from the user
    hours: int = int(input('Please enter a number of credit hours '
                           + 'completed: '))
    print('A student with', hours,
          'hours is classified as a', standing(hours))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))