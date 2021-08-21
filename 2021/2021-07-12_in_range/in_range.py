"""
Given an IPv4 address and a netmask in CIDR notation, return a boolean specifying whether the IP address is inside the given range.

Example:

$ inRange("192.168.4.27", "192.168.0.0/16")
$ true

$ inRange("192.168.4.27", "192.168.1.0/24")
$ false
"""

def as_binary(addr):
    return "".join(f"{int(byte):08b}" for byte in addr.split("."))


def in_range(ip_address, cidr):
    prefix, length = cidr.split("/")
    prefix = as_binary(prefix)
    length = int(length)
    ip_address = as_binary(ip_address)
    return ip_address[:length] == prefix[:length]


def test_example1():
    assert in_range("192.168.4.27", "192.168.0.0/16")


def test_example2():
    assert not in_range("192.168.4.27", "192.168.1.0/24")


def test_non_byte_boundary():
    assert in_range("192.168.1.27", "192.168.1.0/27")
    assert not in_range("192.168.1.127", "192.168.1.0/27")
