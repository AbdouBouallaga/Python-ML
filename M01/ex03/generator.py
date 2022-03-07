def generator(text, sep=" ", option=None):
    import random
    '''Option is an optional arg, sep is mandatory'''
    def valid_option(op):
        valid = ["shuffle", "unique", "ordered"]
        if op is None or op in valid:
            return True
        else:
            return False
    if type(text) is str and type(sep) is str and valid_option(option):
        used = {}
        ret = text.split(sep)
        if option is "ordered":
            ret = sorted(ret)
        if option is "shuffle":
            ret = random.sample(ret, len(ret))
        for wd in ret:
            if option is "unique":
                if wd not in used:
                    yield(wd)
                    used[wd] = 1
            else:
                yield(wd)
    else:
        print("ERROR")
        return(0)
