"""
Given an integer n representing the number of sides of a regular polygon,
return the measure of each interior angle. Bonus points: implement some of the
other functions listed in the linked Wikipedia page!

Example:

$ interior_angle_size(3)
$ 60 // Each angle in a triangle that is a regular polygon is 60 degrees

$ interior_angle_size(8)
$ 135
"""


def interior_angle_size(n_sides):
    """Calculate interior angles of a regular n-gon"""
    exterior = 360 / n_sides
    return 180 - exterior


def test_example1():
    """Test first example"""
    assert interior_angle_size(3) == 60


def test_example2():
    """Test second example"""
    assert interior_angle_size(8) == 135
