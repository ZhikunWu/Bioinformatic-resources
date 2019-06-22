#!/usr/bin/env python
import sys
import math
import scipy.stats as stats

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def fisher_exact_test(a, b, c, d):
    """
    argv:
        [368, 132, 10562, 13480]
    return:
        1.2920236451680064e-40

    There is somethong wrong with the accuracy
    """
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    n = a + b + c + d
    # p_value = ( math.factorial(a+b) * math.factorial(c+d) * math.factorial(a+c) * math.factorial(b+d) ) /  \
    #     ( math.factorial(a) * math.factorial(b) * math.factorial(c) * math.factorial(d) * math.factorial(n) )
    p_value = ( factorial(a+b) * factorial(c+d) * factorial(a+c) * factorial(b+d) ) /  \
        ( factorial(a) * factorial(b) * factorial(c) * factorial(d) * factorial(n) )
    print(p_value)
    return p_value

def stats_fisher_exact(obs):
    """
    argv:
        [[368, 132], [10562, 13480]]
    return:
        2.41127716957e-40
    """
    #gene_numbre: 24042
    # obs = [[368, 132], [10562, 13480]]
    oddsratio, pvalue= stats.fisher_exact(obs)
    print(pvalue)

if __name__ == "__main__":
    fisher_exact_test(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    stats_fisher_exact([[sys.argv[1], sys.argv[2]], [sys.argv[3], sys.argv[4]]])


