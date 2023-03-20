"""
When you’re representing colors in a program, you typically use HEX, RGB, or HSL. Write a program that converts between the different formats.

Example:

$ convert_colour('rgb', 'hex', '(255,0,0)')
$ '#FF0000'

$ convert_colour('hsl', 'rgb', '(65,80,80)')
$ '(238,245,163)'

$ convert_colour('hsl', 'hex', '(65,80,80)')
$ '#EEF5A3'
"""

from math import cos, sin, pi


def convert_colour(in_format, out_format, value):
    r, g, b = parse(in_format, value)
    print(r, g, b)
    return render(out_format, r, g, b)


def parse(in_format, value):
    if in_format == 'rgb':
        return parse_triple(value)
    elif in_format == 'hex':
        return [int(value[i:i+2], 16) for i in range(1, len(value), 2)]
    elif in_format == 'hsl':
        h, s, l = parse_triple(value)
        return hsl_to_rgb(h, s, l)
    else:
        raise ValueError(f"Unknown format {in_format}")


def parse_triple(value):
    return [int(x) for x in value[1:-1].split(',')]


def hsl_to_rgb(h, s, l):
    s = s / 100
    l = l / 100
    def f(n):
        k = (n + h / 30) % 12
        a = s * min(l, 1 - l)
        return l - a * max(-1, min(k - 3, 9 - k, 1)) * 255
    return (f(0), f(8), f(4))


def render(out_format, r, g, b):
    if out_format == 'rgb':
        return f"({r},{g},{b})"
    elif out_format == 'hex':
        return f"#{hex((r << 16) + (g << 8) + b)[2:]}".upper()
    elif out_format == 'hsl':
        h, s, l = rgb_to_hsl(r, g, b)
        return f"({h},{s},{l})"


def rgb_to_hsl(r, g, b):
    return r, g, b


def test_example1():
    assert convert_colour('rgb', 'hex', '(255,0,0)') == '#FF0000'


def test_example2():
    assert convert_colour('hsl', 'rgb', '(65,80,80)') == '(238,245,163)'


def test_example3():
    assert convert_colour('hsl', 'hex', '(65,80,80)') == '#EEF5A3'
