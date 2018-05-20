def bisect_right(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (hi+lo)//2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo


def insort_right(a, x, lo=0, hi=None):
    index = bisect_right(a, x, lo, hi)
    a.insert(index, x)

if __name__ == '__main__':
    a = [1, 3, 5, 9]
    insort_right(a, 4)
    print(a)
    pass