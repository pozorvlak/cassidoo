#!/usr/bin/env python

"""Given a string S containing only digits, write a function that returns a list
containing all possible combinations of valid IPv4 IP addresses."""

def get_ip(s):
    return (".".join(ip) for ip in get_ip_worker(s, 4))


def get_ip_worker(s, n):
    """"Yield partial IP addresses from s with n left to find"""
    if len(s) < n:
        return
    if len(s) > 3 * n:
        return
    if n == 0:
        yield []
        return
    if s[0] == '0':
        # Leading zeros are not allowed, so the next component must be 0
        yield from (['0'] + suffix for suffix in get_ip_worker(s[1:], n-1))
        return
    for i in range(1, len(s) - n + 2):
        prefix = s[:i]
        if int(prefix) < 256:
            yield from ([prefix] + suffix for suffix in get_ip_worker(s[i:], n-1))
