import sys
from bisect import bisect_left as bl
def all_left_truncatable_prime(tup):
    # sort the tuples in ascending order
    tup.sort()
    # get the current value
    val = tup[177][0]
    # generate the list of left-truncatable primes
    res = []
    # create the list of primes
    primes = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 409, 419, 421, 431, 449, 457, 461, 463, 467, 491, 499, 503, 509, 521, 607, 613, 617, 619, 631, 637, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 733, 739, 743, 751, 757, 761, 763, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 833, 839, 853, 857, 859, 863, 867, 871, 873, 883, 887, 907, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    # create the list of left-truncatable primes
    ltr = []
    # for each prime in primes:
    for p in primes:
        # if the prime is left-truncatable:
        if p.islefttruncatable():
            # add it to the list of left-truncatable primes
            ltr.append(p)
    # generate the list of left-truncatable primes less than the current value
    res = [p for p in ltr if p<val]
    # sort the list of left-truncatable primes in ascending order
    res.sort()
    # return the list of left-truncatable primes
    return res
