def char_num_sort(words):
    return sorted(words, key=lambda x: (len(set(x.lower())), -len(x)))


if __name__ == '__main__':
    assert(
        char_num_sort("Bananas do not grow in Mississippi".split())
        == "do in not Mississippi Bananas grow".split()
    )

