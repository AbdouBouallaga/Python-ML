import sys
import string

if __name__ == "__main__":
    av = sys.argv[1:]
    if (len(av) is not 2):
        print("ERROR")
        print('"Usage: > python filterwords.py "Hello, my friend" 3"')
    st = av[0]
    for char in st:
        if char in string.punctuation:
            st = st.replace(char, '')
    tab = st.split(" ")
    ret = filter(lambda x: len(x) > int(av[1]), tab)
    print(list(ret))
