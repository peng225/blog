#!/usr/bin/env sage

from sage.all import *
import sys

def main():
    args = sys.argv
    if len(args) != 2 or not args[1].isdigit():
        print("usage: {} <square free integer>".format(argv[0]))
        sys.exit(1)

    m = int(args[1])
    if not m.is_squarefree():
        print("{} is not square free.".format(m))
        sys.exit(1)

    N = abs(m)
    if m % 4 == 2 or m % 4 == 3:
        N = 4 * abs(m)
    L = CyclotomicField(N)
    # TODO: really must have one generator?
    # I just want zeta_N.
    if len(L.gens()) != 1:
        print("More than 1 generator found for L: {}".format(L.gens()))
        sys.exit(1)
    galois_group = L.galois_group()
    normal_subgroups = galois_group.normal_subgroups()

    quad_sub_field = findQuadraticSubfield(L, m)
    if quad_sub_field is None:
        print("Failed to find quadratic subfield.")
        sys.exit(1)

    for nsg in normal_subgroups:
        # The index of subgroup corresponding to the quadratic field
        # must be 2.
        if subgroupIndex(galois_group, nsg) != 2:
            continue

        if not fixQuadraticSubField(quad_sub_field, nsg):
            continue

        print("Found: {}".format(nsg))
        print(convertToMultGroupOfZOverNZ(nsg, L.gen()))

def findQuadraticSubfield(L, m):
    K.<sqrt_m> = QuadraticField(m)
    for sub in L.subfields(2):
        if sub[0].is_isomorphic(K):
            return sub[0]
    return None

def subgroupIndex(G, SG):
    return G.order() / SG.order()

def fixQuadraticSubField(quad_sub_field, galois_subgroup):
    gens = quad_sub_field.gens()
    for e in galois_subgroup:
        for g in gens:
            if e(g) != g:
                return False
    return True

def convertToMultGroupOfZOverNZ(galois_subgroup, zeta_N):
    ret = []
    for e in galois_subgroup:
        tmp= e(zeta_N)
        n = 0
        while tmp != 1:
            tmp = tmp / zeta_N
            n += 1
        ret.append(n)
    return ret

if __name__ == "__main__":
    main()
