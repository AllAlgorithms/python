# Python implementation of Bogo sort

from random import shuffle

def bogo_sort(l):
    while not all(l[i] <= l[i+1] for i in xrange(len(l)-1)):
        shuffle(l)
    return l

# Tests
if __name__ == '__main__':
    print bogo_sort([3, 2, 1])
    print bogo_sort([1000, 100, 10, 1])
