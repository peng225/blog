#!/usr/bin/env sage

from sage.all import *

def main():
    V = FiniteRankFreeModule(GF(4), 3, name='M', start_index=1)
    print(f"V: {V}")
    basis = V.basis('e')
    print(f"basis: {basis}")

    print(f"V^*: {V.dual()}")
    dual_basis = basis.dual_basis()
    print(f"dual_basis: {dual_basis}")

    for i, e in enumerate(basis):
        for j, f in enumerate(dual_basis):
            print(f"f_{j+1}(e_{i+1}) = {f(e)}")

if __name__ == "__main__":
    main()
