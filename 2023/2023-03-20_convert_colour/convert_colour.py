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
    c = (1 - abs(2*l - 1)) * s
    x = c * (1 - abs((h/60) % 2 - 1))
    m = l - c/2
    if h < 60:
        r, g, b = c, x, 0
    elif h < 120:
        r, g, b = x, c, 0
    elif h < 180:
        r, g, b = 0, c, x
    elif h < 240:
        r, g, b = 0, x, c
    elif h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    return [int(255*(r+m)), int(255*(g+m)), int(255*(b+m))]


def render(out_format, r, g, b):
    if out_format == 'rgb':
        return f"({r},{g},{b})"
    elif out_format == 'hex':
        return f"#{hex((r << 16) + (g << 8) + b)[2:]}".upper()
    elif out_format == 'hsl':
        h, s, l = rgb_to_hsl(r, g, b)
        return f"({h},{s},{l})"


def rgb_to_hsl(r, g, b):
    r = r / 255
    g = g / 255
    b = b / 255
    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min
    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * (((b - r) / delta) + 2)
    elif c_max == b:
        h = 60 * (((r - g) / delta) + 4)
    l = (c_max + c_min) / 2
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2*l - 1))
    return [int(h), int(s*100), int(l*100)]


def test_example1():
    assert convert_colour('rgb', 'hex', '(255,0,0)') == '#FF0000'


def test_example1_inverse():
    assert convert_colour('hex', 'rgb', '#FF0000') == '(255,0,0)'


def test_example2():
    assert convert_colour('hsl', 'rgb', '(65,80,80)') == '(238,245,163)'


def test_example2_inverse():
    assert convert_colour('rgb', 'hsl', '(238,245,163)') == '(65,80,80)'


def test_example3():
    assert convert_colour('hsl', 'hex', '(65,80,80)') == '#EEF5A3'


def test_example3_inverse():
    assert convert_colour('hex', 'hsl', '#EEF5A3') == '(65,80,80)'
