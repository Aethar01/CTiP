#!/usr/bin/env python3

import random
import numpy as np


def p1(n, k):
    print(f"\n n = {n}, k = {k}")
    for k in range(1, k):
        c = 0
        for i in range(0, n):
            x = random.uniform(0, 1)
            phi = np.pi*random.uniform(0, 1)
            sx = 0.5*np.sin(phi)
            if (x < sx or 1-x < sx):
                c += 1
        print(k, float(c)/n, 2./np.pi, float(c)/n - 2./np.pi)


def main():
    n = (10**2, 10**3, 10**4, 10**5, 10**6)
    k = (10, 100, 1000)
    for i in n:
        for j in k:
            p1(i, j)


if __name__ == '__main__':
    main()
