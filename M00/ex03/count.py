def text_analyzer(*arv):
    """This function counts the number of upper characters, lower characters, \
punctuation and spaces in a given text."""
    if len(arv) > 1:
        print("ERROR")
        return
    if len(arv) == 0:
        print("What is the text to analyse?")
        str = input()
    else:
        str = arv[0]
    import string

    up = 0
    low = 0
    punc = 0
    space = 0
    total = 0
    puncs = string.punctuation
    for c in str:
        total += 1
        if c.islower():
            low += 1
        elif c.isupper():
            up += 1
        elif c in puncs:
            punc += 1
        elif c.isspace:
            space += 1
    print("The text contains", total, "characters:")
    print(up, "upper letters")
    print(low, "lower letters")
    print(punc, "punctuation marks")
    print(space, "spaces")
