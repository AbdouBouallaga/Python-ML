class Evaluator():
    def zip_evaluate(coefs, words):
        if len(words) is not len(coefs):
            return -1
        ret = 0
        for w, c in zip(words, coefs):
            ret += len(w) * c
        return ret

    def enumerate_evaluate(coefs, words):
        if len(words) is not len(coefs):
            return -1
        ret = 0
        for i, w in enumerate(words):
            ret += len(w) * coefs[i]
        return ret
