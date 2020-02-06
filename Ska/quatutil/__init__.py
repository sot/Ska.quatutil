# Licensed under a 3-clause BSD style license - see LICENSE.rst

__version__ = '3.3.2'

from .quatutil import *  # noqa


def test(*args, **kwargs):
    '''
    Run py.test unit tests.
    '''
    import testr
    return testr.test(*args, **kwargs)