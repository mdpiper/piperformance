"""A very rough processor performance test."""

import platform
import time
from tqdm import tqdm
from decimal import Decimal, getcontext


def pi():
    """Compute pi to the current precision.

    Copied from https://docs.python.org/3/library/decimal.html#recipes

    >>> print(pi())
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision


class Timer(object):
    def __init__(self, title=None):
        self.title = title
        self.start = 0.

    def __enter__(self):
        if self.title:
            print(self.title)
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        print(f"Elapsed time: {round(time.time() - self.start, 3)} s")


def run(iter=1000):
    with Timer(title=platform.version()):
        for _ in tqdm(range(iter)):
            for _ in range(iter):
                pi()


if __name__ == "__main__":
    print("\n... p i p e r f o r m a n c e ...\n")
    run(iter=500)
