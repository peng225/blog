#!/usr/bin/env sage

from sage.all import *
import sys

def main():
    args = sys.argv
    if len(args) != 2 or not is_integer(args[1]):
        print("usage: {} <square free integer>".format(args[0]))
        sys.exit(1)

    m = Integer(args[1])
    if m == 1:
        print("m should not be 1 by definition of quadratic field.")
        sys.exit(1)

    if not m.is_squarefree():
        print("{} is not square free.".format(m))
        sys.exit(1)

    N = abs(m)
    if m % 4 == 2 or m % 4 == 3:
        N = 4 * abs(m)
    print("N: {}".format(N))
    L = CyclotomicField(N)
    galois_group = L.galois_group()
    # Because Q(sqrt{m})/Q is Galois extension,
    # the corresponding subgroup of Gal(Q(zeta_N)/Q)
    # must be a normal subgroup.
    normal_subgroups = galois_group.normal_subgroups()

    quad_sub_field = find_quadratic_subfield(L, m)
    if quad_sub_field is None:
        print("Failed to find quadratic subfield.")
        sys.exit(1)

    for nsg in normal_subgroups:
        # The index of subgroup corresponding to the quadratic field
        # must be 2.
        if subgroup_index(galois_group, nsg) != 2:
            continue

        if not fix_quadratic_subfield(quad_sub_field, nsg):
            continue

        print("Galois subgroup: {}".format(nsg))
        print("Corresponding element(s) in (Z/NZ)^x: {}".format(convert_to_mult_group_of_Z_over_NZ(nsg, L.gen())))

def is_integer(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

def find_quadratic_subfield(cyclotomic_field, m):
    K = QuadraticField(m)
    for sub in cyclotomic_field.subfields(2):
        if sub[0].is_isomorphic(K):
            return sub[0]
    return None

def subgroup_index(group, subgroup):
    return group.order() / subgroup.order()

def fix_quadratic_subfield(quad_sub_field, galois_subgroup):
    gens = quad_sub_field.gens()
    for e in galois_subgroup:
        for g in gens:
            if e(g) != g:
                return False
    return True

def convert_to_mult_group_of_Z_over_NZ(galois_subgroup, zeta_N):
    ret = []
    for e in galois_subgroup:
        tmp = e(zeta_N)
        # tmp is in form of zeta_N^n.
        # The follow calculation is finding n.
        n = 0
        while tmp != 1:
            tmp = tmp / zeta_N
            n += 1
        ret.append(n)
    ret.sort()
    return ret

if __name__ == "__main__":
    main()
