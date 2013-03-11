#!/usr/bin/env python

from pjohansson.session7 import count_uniques, factorise, histogram
from IPython.parallel import Client
from multiprocessing import Pool

import multiprocessing
import sys

# Get and check option
try:
    _, mode = sys.argv
except ValueError:
    mode = 'h'
if mode not in 'smi':
    print "usage: factorise.py mode"
    print
    print "mode:"
    print "  s for serial"
    print "  m for multiprocessing"
    print "  i for IPython"
    exit()


# Start factorisation
start = 2
end = 500000
uniques = []

if mode == 's':
    for number in range(start, end + 1):
        factors = factorise(number)
        uniques.append(count_uniques(factors))

elif mode == 'm':
    def worker(number):
        factors = factorise(number)
        return count_uniques(factors)

    pool = Pool(processes=multiprocessing.cpu_count())
    result = pool.map_async(worker, range(start, end + 1))
    uniques = result.get()

elif mode == 'i':
    try:
        cli = Client()
    except IOError:
        print "no engines started: ipcluster start -n [NUM]"
        exit()
    dview = cli[:]

    # Import functions on engines
    with dview.sync_imports(quiet=True):
        from pjohansson.session7 import factorise, count_uniques

    @dview.parallel(block=True)
    def worker(number):
        factors = factorise(number)
        return count_uniques(factors)

    uniques = worker.map(range(start, end + 1))

# Output as plain dictionary
print histogram(uniques)
