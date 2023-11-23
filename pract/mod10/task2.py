import re
import doctest

def is_valid_rgb(color):
    """
    >>> is_valid_rgb('rgb(255, 255, 255)')
    True
    >>> is_valid_rgb('rgb(10%, 20%, 0%)')
    True
    >>> is_valid_rgb('rgb(257, 50, 10)')
    False
    """
    pattern = re.compile(r'^rgb\((\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), (\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), (\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?)\)$')
    return bool(pattern.match(color))

def is_valid_hex(color):
    """
    >>> is_valid_hex('#2345')
    False
    >>> is_valid_hex('ffffff')
    False
    >>> is_valid_hex('#21f48D')
    True
    >>> is_valid_hex('#888')
    True
    """
    pattern = re.compile(r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$')
    return bool(pattern.match(color))


def is_valid_hsl(color):
    """
    >>> is_valid_hsl('hsl(200,100%,50%)')
    True
    >>> is_valid_hsl('hsl(34%, 20%, 50%)')
    False
    >>> is_valid_hsl('hsl(0, 0%, 0%)')
    True
    >>> is_valid_hsl('hsl(20, 10, 0.5)')
    False
    """
    pattern = re.compile(r'^hsl\((\d{1,3}|[1-9]\d{0,2}),\s*(100%|[1-9]?\d%|0%),\s*(100%|[1-9]?\d%|0%)\)$')
    return bool(pattern.match(color))

doctest.testmod()