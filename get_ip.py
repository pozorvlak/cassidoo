#!/usr/bin/env python

"""Given a string S containing only digits, write a function that returns a list
containing all possible combinations of valid IPv4 IP addresses."""

def get_ip(s):
    return (".".join(ip) for ip in get_ip_worker(s, 4))


def get_ip_worker(s, n):
    """"Yield partial IP addresses from s with n left to find"""
    if n == 0 and len(s) > 0:
        return
    if n == 0 and len(s) == 0:
        yield []
        return
    if len(s) < n:
        return
    for i in range(1, 4):
        prefix = s[:i]
        if int(prefix) < 256:
            # TODO strip out leading zeros
            yield from ([prefix] + suffix for suffix in get_ip_worker(s[i:], n-1))
