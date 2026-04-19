import re

def is_valid_username(username):
    if not username:
        return False
    return 3 <= len(username) <= 20 and re.match('^[a-zA-Z][a-zA-Z0-9_]*$', username)


def is_valid_password(password):
    if not password:
        return False
    return (
        len(password) >= 8 and
        re.search('[A-Z]', password) and
        re.search('[a-z]', password) and
        re.search('[0-9]', password)
    )


def is_valid_email(email):
    if not email:
        return False
    regex = ('^[a-z0-9]+[._%+-]*[a-z0-9]*@[a-z0-9]+[-]?[a-z0-9]+\.[a-z]{2,}$')
    return re.match(regex, email) is not None


def is_positive_integer(value):
    return isinstance(value, int) and value > 0


def is_valid_coord(x, y):
    return is_positive_integer(x) and is_positive_integer(y)