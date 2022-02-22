import sys


def swap(str):
    print(str.swapcase()[::-1], end='')


args = sys.argv[1:]
args = args[::-1]
deb = 0


if len(args):
    for s in args:
        if deb:
            print(" ", end='')
        swap(s)
        deb += 1
    print()
