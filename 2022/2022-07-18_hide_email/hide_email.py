"""
Given a string that has a valid email address, write a function to hide the first part of the email (before the @ sign), minus the first and last character. For extra credit, add a flag to hide the second part after the @ sign to your function excluding the first character and the domain extension.

Examples:

> hideEmail('example@example.com')
> 'e*****e@example.com'

> hideEmail('example+test@example.co.uk', hideFull)
> 'e**********t@e******.co.uk'
"""


def hide_name(word):
    return word[0] + ('*' * (len(word) - 2)) + word[-1]


def hide_domain(domain):
    bits = domain.split('.')
    bits[0] = bits[0][0] + '*' * (len(bits[0]) - 1)
    return '.'.join(bits)


def hide_email(email, hide_full=False):
    name, domain = email.split('@')
    name = hide_name(name)
    if hide_full:
        domain = hide_domain(domain)
    return name + '@' + domain


def test_example1():
    assert hide_email('example@example.com') == 'e*****e@example.com'


def test_example2():
    assert hide_email('example+test@example.co.uk', hide_full=True) == \
            'e**********t@e******.co.uk'
