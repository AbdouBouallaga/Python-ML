t = (3, 30, 2019, 9, 25)

if __name__ == "__main__":
    date = t[:3]
    time = t[3:]
    print(*date, sep="/", end=" ")
    print(*time, sep=":")
