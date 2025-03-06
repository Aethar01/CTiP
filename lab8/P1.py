#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp


# derivative by finite difference
def dC(Nmax, Tmax, C):
    for T in range(0, Tmax):
        for N in range(1, Nmax-1):
            C[N] = (C[N-1] + C[N+1]) / 2
    return C


def Ctheory(Nmax, Tmax):
    values = [0 for _ in range(0, Nmax)]
    for T in range(0, Tmax):
        for N in range(0, Nmax):
            values[N] = N * sp.erfc(N/np.sqrt(2 * T))
    return values


def plot(x, y, title):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("C(x, t)")
    plt.show()


def main():
    Nmax = 20
    Tmax = 100
    C = [0 for _ in range(0, Nmax)]
    C[0] = 100
    x = np.arange(Nmax)
    y = dC(Nmax, Tmax, C)
    ytheory = Ctheory(Nmax, Tmax)
    plot(x, y, "Numerical Solution")
    plot(x, ytheory, "Theoretical Solution")


if __name__ == "__main__":
    main()
