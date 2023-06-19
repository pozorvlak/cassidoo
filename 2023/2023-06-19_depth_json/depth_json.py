"""
Given some JSON data, calculate the maximum depth reached. Both arrays and
dictionaries increase the depth! If the input is invalid data, the response
should be undefined (you decide how you want that to return).

Example:

> depth_json([])
> 1

> depth_json([1, 2, 3, 4, 5])
> 1

> depth_json([{"a": []}, ["abc"]])
> 3
"""

def depth_json(data):
    if isinstance(data, list):
        if len(data) == 0:
            return 1
        return max(depth_json(d) for d in data) + 1
    elif isinstance(data, dict):
        if len(data) == 0:
            return 1
        return max(depth_json(v) for v in data.values()) + 1
    else:
        return 0


def test_example1():
    assert depth_json([]) == 1


def test_example2():
    assert depth_json([1, 2, 3, 4, 5]) == 1


def test_example3():
    assert depth_json([{"a": []}, ["abc"]]) == 3
