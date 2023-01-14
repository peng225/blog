#!/usr/bin/env sage

import sys
from sage.all import *

def printUsage():
    print(f"usage: {sys.argv[0]} order dim")

def main():
    if len(sys.argv) != 3:
        printUsage()
        sys.exit(1)

    order = int(sys.argv[1])
    dim = int(sys.argv[2])

    print(f"order = {order}, dim = {dim}")

    for i in range(order):
        print(f"i = {i}")
        field = GF(order)
        gen = field.gen()
        vec = [1, i, gen]
        V = VectorSpace(field,dim)
        S = V.subspace([V(vec)])
        print(f"S: {S}")
        oc = S.complement()
        print(f"oc: {oc}")
        ococ = oc.complement()
        print(f"ococ: {ococ}")
        print(f"intersection:  {oc.intersection(ococ)}")

if __name__ == "__main__":
    main()
