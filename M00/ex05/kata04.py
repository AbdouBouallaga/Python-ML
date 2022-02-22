t = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
    print("module_0%d" % t[0], end=", ")
    print("ex_0%d" % t[1], end=" : ")
    print("{:.2f}".format(t[2]), end="")
    for n in t[3:]:
        print(end=", ")
        print("{:.2e}".format(n), end="")
    print()
