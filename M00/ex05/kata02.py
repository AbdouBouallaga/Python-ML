t = (3, 30, 2019, 9, 25)

if __name__ == "__main__":
    date = t[:3]
    mnt = str(date[0]).zfill(2)
    day = str(date[1]).zfill(2)
    year = str(date[2])
    time = t[3:] 
    hour = str(time[0]).zfill(2)
    minute = str(time[1]).zfill(2)
    print(mnt, day, year, sep="/", end=" ")
    print(hour, minute, sep=":")
