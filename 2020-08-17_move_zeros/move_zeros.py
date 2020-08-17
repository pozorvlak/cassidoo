def move_zeros_generator(xs):
    num_zeros = 0
    for x in xs:
        if x == 0:
            num_zeros += 1
        else:
            yield x
    for i in range(num_zeros):
        yield 0


def move_zeros(xs):
    return list(move_zeros_generator(xs))


def move_zeros_inplace(xs):
    num_zeros = 0
    for i, x in enumerate(xs):
        if x != 0:
            xs[i - num_zeros] = x
        else:
            num_zeros += 1
    for i in range(-num_zeros, 0):
        xs[i] = 0


# Not O(n), but cute :-)
def move_zeros_short(xs):
    return sorted(xs, key=lambda x: x == 0)
