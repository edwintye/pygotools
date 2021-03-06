''' gradient

.. moduleauthor:: Edwin Tye <Edwin.Tye@gmail.com>

'''

from __future__ import division, print_function, absolute_import

from .optimTestFun import *
from .consMani import *
from .optCondition import *

__all__ = [s for s in dir() if not s.startswith('_')]
from numpy.testing import Tester
test = Tester().test
