import sys

args = sys.argv[1:]
num = None

if len(args) > 1:
    print("AssertionError: more than one argument is provided")

if len(args) == 1:
    try:
        num = float(args[0])
    except Exception:
        print("AssertionError: argument is not integer")
    finally:
        if num is not None:
            if num == 0:
                print("I’m Zero.")
            elif num % 2:
                print("I’m Odd.")
            else:
                print("I’m Even.")
print()
