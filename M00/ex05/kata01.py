languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
}


def outp(frag):
    print(frag, "was created by", languages[frag])


if __name__ == "__main__":
    for frag in languages:
        outp(frag)
