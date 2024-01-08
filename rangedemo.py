def main(args: list[str]) -> int:
    # Simple range(stop).  
    # From 0 up to, but not including, the one argument STOP.
    print('range(9) =', list(range(9)))
    print('range(15) =', list(range(15)))

    # Two-argument range(start, stop).
    # From START up to, but not including, STOP.
    print('range(0,9) =', list(range(0, 9))) # 0 through 8
    print('range(1,9) =', list(range(1, 9))) # 1 through 8
    print('range(10,15) =', list(range(10, 15))) # 10 through 14

    # Three-argument range(start, stop, step).
    # Count from START to, but not including, STOP with step size STEP
    print('range(10, -1, -1) =', list(range(10, -1, -1))) # 10 down to 0
    print('range(0, 101, 10) =', list(range(0, 101, 10))) # 0 through 100 by 10's
    print('range(31, 50, 2) =', list(range(31, 50, 2))) # odd numbers betwenn 30 and 50
    print('range(30, 61, 3) =', list(range(30, 61, 3))) # multiples of 3 from 30 through 60



    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))