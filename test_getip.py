from get_ip import get_ip


def test_example():
    ips = set(get_ip('11211'))
    assert ips == set([
        '1.1.2.11',
        '1.1.21.1',
        '1.12.1.1',
        '11.2.1.1',
    ])

