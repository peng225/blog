#!/usr/bin/python3

from sympy.functions.combinatorial.numbers import stirling
from sympy.functions.combinatorial.numbers import nC
import matplotlib.pyplot as plt
import sys
import math

def coupon(k, l, n):
    loopNum = min(n-k+l, l)+1

    numPattern = 0
    for i in range(loopNum):
        stir = stirling(n-1, k-l-1+i, kind=2)
        numPattern += (k-l) * nC(l, i) * math.factorial(k-l-1+i) * stir
    return float(numPattern) / k**n

def main():
    argv = sys.argv
    if len(argv) < 2 or 3 < len(argv):
        print(f"usage: {argv[0]} numCouponKind [isCumulative]")
        sys.exit(1)

    numCouponKind = int(argv[1])
    isCumulative = (len(argv) == 3 and (argv[2] == "True" or argv[2] == "true"))
    numTrial = 30
    for l in range(0, numCouponKind):
        x = []
        y = []
        cumulativeProb = 0
        for n in range(1, numTrial+1):
            prob = coupon(numCouponKind, l, n)
            cumulativeProb += prob
            x.append(n)
            if isCumulative:
                y.append(cumulativeProb)
            else:
                y.append(prob)
        plt.plot(x, y, label='l = {}'.format(l))
    plt.legend()
    plt.grid()
    plt.xlabel("n")
    plt.ylabel("probability")
    # plt.savefig('coupon_lx_k' + str(numCouponKind) + '.png')
    plt.show()

if __name__ == "__main__":
    main()
