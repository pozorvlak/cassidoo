"""
Given a string of brackets, return a rotation of those brackets that is
balanced. The numbers of opening and closing brackets will always be equal, so
[ or ][] won’t be given as inputs.

Example:

$ rotateBrackets(‘]][][[‘)
$ ‘[[]][]’ // First rotation yields ‘[]][][‘. Second one yields ‘[[]][]’.
"""

from hypothesis import given
import hypothesis.strategies as st


def rotate_brackets(s):
    if s == "":
        return s
    nesting, remaining_opens, remaining_closes = 0, len(s) / 2, len(s) / 2
    # idea: loop over string, and for each point x find
    #  1. net number of opens after x
    #  2. net number of closes before x
    #  3. does nesting level go negative after x?
    # if #1 == #2 and #3 is false, x is a possible starting point.
    closes_count = 0
    net_closes = []
    for i, c in enumerate(s):
        net_closes.append(closes_count)
        if c == ']':
            closes_count += 1
        elif c == '[':
            closes_count -= 1
    opens_count = 0
    net_opens = []
    for i in reversed(range(len(s))):
        c = s[i]
        if c == '[':
            opens_count += 1
        elif c == ']':
            opens_count -= 1
        net_opens.insert(0, opens_count)
    for i in (reversed(range(len(s)))):
        if max_net_opens[i] == max_net_closes[i] >= 0:
            return s[i:] + s[:i]
    print(f"Couldn't find solution for {s}")
    print(f"{net_closes=}, {net_opens=}, {has_gone_negatives=}")


def is_balanced(s):
    nesting = 0
    scores = {'[': 1, ']': -1}
    for c in s:
        nesting += scores[c]
        if nesting < 0:
            return False
    return nesting == 0


def oracle(s):
    if s == "":
        return s
    for i in reversed(range(len(s))):
        candidate = s[i:] + s[:i]
        if is_balanced(candidate):
            return candidate
    print(f"Couldn't find solution for {s}")


def test_example():
    assert rotate_brackets(']][][[') == '[[]][]'


@st.composite
def bracket_string(draw):
    xs = draw(st.lists(st.sampled_from([1, -1])))
    error = sum(xs)
    if error < 0:
        xs += [1] * abs(error)
    elif error > 0:
        xs += [-1] * error
    assert sum(xs) == 0
    return "".join([" []"[x] for x in xs])


@given(bracket_string())
def test_is_balanced(s):
    assert is_balanced(rotate_brackets(s))


@given(bracket_string())
def test_oracle(s):
    assert rotate_brackets(s) == oracle(s)
