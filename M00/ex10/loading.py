from timeit import timeit


def clr():
    print("\033c", end="")

i = 0

def ft_progress(lst):
    print(lst)
    #print("\033c", end="")
    try:
        if start:
            nothing = 1;
    except Exception:
        start = timeit()
    print()


if __name__ == "__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
