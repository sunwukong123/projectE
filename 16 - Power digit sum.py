# -*- coding: utf-8 -*-
"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

from functools import reduce

n = pow(2, 1000)

s = str( n )

l = list( s )

print( reduce( lambda x, y: int(x) + int(y), l ) )