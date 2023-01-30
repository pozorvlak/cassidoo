"""
You are given a list of positive integers which represents some range of
integers which has been truncated. Find the missing bits, insert ellipses to
show that that part has been truncated, and print it. If the consecutive values
differ by exactly two, then insert the missing value.

Examples:

> missing_bits([1,2,3,4,20,21,22,23])
> "[1,2,3,4,...,20,21,22,23]"

> missing_bits([1,2,3,5,6])
> "[1,2,3,4,5,6]"

> missing_bits([1,3,20,27])
> "[1,2,3,...,20,...,27]"
"""

def missing_bits(bits):
    if bits == []:
        return "[]"
    last_bit = bits.pop(0)
    strbits = [str(last_bit)]
    for bit in bits:
        diff = bit - last_bit
        if diff == 2:
            strbits.append(str(bit - 1))
        elif diff > 2:
            strbits.append("...")
        strbits.append(str(bit))
        last_bit = bit
    return "[" + ",".join(strbits) + "]"


def test_example1():
    assert missing_bits([1,2,3,4,20,21,22,23]) == "[1,2,3,4,...,20,21,22,23]"


def test_example2():
    assert missing_bits([1,2,3,5,6]) == "[1,2,3,4,5,6]"


def test_example3():
    assert missing_bits([1,3,20,27]) == "[1,2,3,...,20,...,27]"
