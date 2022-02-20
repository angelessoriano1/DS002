# -*- coding: utf-8 -*-
"""Stats.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fJDUsWxheo5lDH-VOZi5U2czhik1Dmla
"""

from typing import List
from collections import Counter

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


# The underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library.
def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
    """Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

def quantile(xs: List[float],p: float) -> float:
  # returns the th-percentile value in x
  p_index = int(p * len(xs))
  return sorted (xs)[p_index]


def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

# range already means something in python, so we'll use a different name 
def data_range(xs: List[float]) -> float:
  return max(xs) - min(xs)

def interquartile_range(xs: List[float]) -> float:
  #returns the difference between the 75rg-ile and the 25%-ile 
  return quantile(xs, 0.75) - quantile(xs, 0.25)
