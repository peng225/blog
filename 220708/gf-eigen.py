#!/usr/bin/env sage

from sage.all import *

def main():
    matrixList = []
    matrixList.append(matrix(GF(3), [[2, 1], [1, 2]]))
    matrixList.append(matrix(GF(3), [[2, 0], [0, 2]]))
    matrixList.append(matrix(GF(3), [[2, 1], [0, 2]]))
    matrixList.append(matrix(GF(2), [[1, 1], [1, 0]]))
    # matrixList.append(matrix(GF(4), [[1, 0], [0, 1]]))
    for mat in matrixList:
        # try:
        print(f"matrix:\n{mat}")
        print(f"eigen values: {mat.eigenvalues()}")
        print("eigen vectors(right):")
        for ev in mat.eigenvectors_right():
            print(ev)
        print("eigen spaces(right):")
        for es in mat.eigenspaces_right():
            print(es)
        # except NotImplementedError:
        #     print("NotImplementedError occurred.")

        print("")

if __name__ == "__main__":
    main()
