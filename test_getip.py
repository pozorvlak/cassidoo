from ipaddress import IPv4Address, AddressValueError

from hypothesis import given
from hypothesis.strategies import integers, ip_addresses

from get_ip import get_ip


def is_ip(s):
    try:
        ip = IPv4Address(s)
        return True
    except AddressValueError:
        return False


def no_dots(ip):
    return "".join(ip.split("."))


@given(integers(0, 999))
def test_no_ips_if_too_small(n):
    ips = list(get_ip(str(n)))
    assert ips == []


@given(integers(1000, 300000000000))
def test_all_are_ips(n):
    ips = list(get_ip(str(n)))
    for ip in ips:
        assert is_ip(ip)


@given(integers(1000, 300000000000))
def test_concatenate_answers(n):
    s = str(n)
    ips = list(get_ip(str(n)))
    for ip in ips:
        assert no_dots(ip) == s


@given(ip_addresses(v=4))
def test_answer_contains_ip(ip):
    s = str(ip)
    ips = list(get_ip(no_dots(s)))
    assert s in ips


def test_example():
    ips = set(get_ip('11211'))
    assert ips == set([
        '1.1.2.11',
        '1.1.21.1',
        '1.12.1.1',
        '11.2.1.1',
    ])

