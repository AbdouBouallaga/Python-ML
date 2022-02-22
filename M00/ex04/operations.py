import sys


def usage():
    print("""Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) > 2:
        print("InputError: too many arguments", end='\n\n')
        usage()
    elif len(args) is not 2:
        usage()
    elif not args[0].isdigit() or not args[1].isdigit():
        print("InputError: only numbers", end='\n\n')
        usage()
    else:
        args[0] = int(args[0])
        args[1] = int(args[1])
        print("Sum:", end='\t\t')
        print(args[0] + args[1])
        print("Difference:", end='\t')
        print(args[0] - args[1])
        print("Product:", end='\t')
        print(args[0] * args[1])
        if args[1] is not 0:
            quoti = args[0] / args[1]
            remai = args[0] % args[1]
        else:
            quoti = "ERROR (div by zero)"
            remai = "ERROR (modulo by zero)"
        print("Quotient:", end='\t')
        print(quoti)
        print("Remainder:", end='\t')
        print(remai)
