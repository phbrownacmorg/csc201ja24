# Read a Social Security number from the keyboard, and print out
# whether it is (potentially) a valid number, using the post-2011
# rules (see https://en.wikipedia.org/wiki/Social_Security_number or
# https://www.ssa.gov/kc/SSAFactSheet--IssuingSSNs.pdf)

def valid_ssn_1(ssn: str) -> bool:
    """Returns a Boolean indicating whether the given string SSN is potentially a valid
    Social Secuity number (including dashes) under the post-2011 rules.  Criteria:
       - The string is 11 characters long.
       - Characters in locations 3 and 6 are hyphens.
       - Everything else is a digit.
       - Area number (first three digits) cannot be 000, 666, or 900-999
       - Group number (fourth and fifth digits) cannot be 00
       - Serial number (last four digits) cannot be 0000
       - Not on a list of known published numbers (078-05-1120, 457-55-5462)"""
    valid = True

    if len(ssn) != 11:
        valid = False
    elif ssn[3] != '-' or ssn[6] != '-':
        valid = False
    elif not (ssn.replace('-', '').isdigit()): 
        valid = False
    elif ssn[0] == '9' or ssn[:3] in ['000', '666']:
        valid = False
    elif ssn[4:6] == '00':
        valid = False
    elif ssn[-4:] == '0000':
        valid = False
    elif ssn in ['078-05-1120', '457-55-5462']:
        valid = False
    
    return valid

def valid_ssn(ssn: str) -> bool:
    """Returns a Boolean indicating whether the given string SSN is potentially a valid
    Social Secuity number (including dashes) under the post-2011 rules.  Criteria:
       - The string is 11 characters long.
       - Characters in locations 3 and 6 are hyphens.
       - Everything else is a digit.
       - Area number (first three digits) cannot be 000, 666, or 900-999
       - Group number (fourth and fifth digits) cannot be 00
       - Serial number (last four digits) cannot be 0000
       - Not on a list of known published numbers (078-05-1120, 457-55-5462)"""
    valid = (len(ssn) == 11)
    valid = valid and ssn[3] == '-' and ssn[6] == '-'
    valid = valid and (ssn[:3] + ssn[4:6] + ssn[-4:]).isdigit()
    valid = valid and ssn[0] != '9' and ssn[:3] not in ['000', '666']
    valid = valid and ssn[4:6] != '00' and ssn[-4:] != '0000'
    valid = valid and ssn not in ['078-05-1120', '457-55-5462']
    
    return valid



def main(args: list[str]) -> int:

    ssn: str = input('Please input a Social Security number, including dashes: ')
    print('"{}" is'.format(ssn), end=' ')

    if not valid_ssn(ssn):
        print('NOT', end=' ')
    print('a valid Social Security number.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))