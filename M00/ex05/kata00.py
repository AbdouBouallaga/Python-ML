t = (19, 42, 21)

if __name__ == "__main__":
    print("The", len(t), "numbers are: ", end='')
    print(*t, sep=", ")
