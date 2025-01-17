from typing import Union, Iterable
from functools import reduce
import math


# Union types
Num = Union[int, float]


def geometric_mean(values: Iterable[Num]) -> float:
    return reduce(lambda x,y: x*y, values)**(1/(len(values)))


def mean(values: Iterable[Num]) -> float:
    """
    For testing, use statistics.mean instead
    """
    return sum(values)/(len(values))


def information_content(frequency: Num) -> float:
    if frequency == 0 or frequency == 1:
        ic = float(0)
    else:
        ic = -(math.log(frequency))
    return ic


def binomial_coeff(num):
    return (num * (num + 1)) / 2