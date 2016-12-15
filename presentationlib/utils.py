import re
import types
from itertools import chain

from . import config

try:
    str_ = (str, unicode)
except NameError:
    str_ = str

container = (list, tuple)


def boxify(s, width):
    """Prints text inside a box with a specified width"""
    # top and bottom
    sides = ['+'.ljust(width - 1, '-') + '+']
    # blank line after top and before bottom
    pad = ['']
    lines = chain(pad, s.splitlines(), pad)
    # add | before and after each line
    modstr = ('|  ' + line.ljust(width - 4, ' ') + '|' for line in lines)

    return '\n'.join(chain.from_iterable([sides, modstr, sides]))


def is_generator(obj):
    iter_py2 = hasattr(obj, 'next')
    iter_py3 = hasattr(obj, '__next__')
    gen = isinstance(obj, types.GeneratorType)
    return iter_py2 or iter_py3 or gen


def split_iter(s, sep):
    return (x.group(0) for x in re.finditer(r'{}', s))
