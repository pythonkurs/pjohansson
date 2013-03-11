def count_uniques(factors):
    """Returns number of unique factors."""

    count = 0
    while factors:
        factor = factors.pop()
        count += 1
        for _ in range(factors.count(factor)):
            factors.pop()

    return count

def factorise(n):
    """Factorise an input integer n."""

    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p

        if r == 0:
            factors.append(p)
            n /= p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1

def histogram(unique):
    """Returns a histogram of counts of unique values as a dictionary."""

    hist = {}
    for value in unique:
        if value in hist.keys():
            hist[value] += 1
        else:
            hist[value] = 1

    return hist
