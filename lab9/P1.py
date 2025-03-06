#!/usr/bin/env python3

import numpy as np
import scipy.integrate as spi


def f1(t, y):
    return -0.5 * (y**2) * t


def f1analytic(t, y0):
    c = - 4/y0
    return -4/(-t**2 + c)


def f2(t, y):
    return -0.5 * t


def f2analytic(t, y0):
    c = y0
    return -0.25 * t**2 + c


def f3(t, y):
    return t * (1 + y)


def f3analytic(t, y0):
    c = np.log(y0 + 1)
    return -1 + np.exp(t**2 / 2 + c)


def plot(ts, ys, ta, ya, title, log=False):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2, 1, sharex=True)
    ax[0].plot(ts, ys, label="RK45", color="red")
    ax[1].plot(ta, ya, label="Analytic", color="blue")
    plt.xlabel("t")
    ax[0].set_ylabel("y")
    ax[1].set_ylabel("y")
    plt.title(title)
    if log:
        ax[0].set_yscale("log")
        ax[1].set_yscale("log")
    ax[0].legend()
    ax[1].legend()
    plt.show()


def main():
    t_span = (0, 10)
    y0 = [3]
    t_eval = np.linspace(*t_span, 100)
    sol1 = spi.solve_ivp(f1, t_span, y0, t_eval=t_eval)
    sol2 = spi.solve_ivp(f2, t_span, y0, t_eval=t_eval)
    sol3 = spi.solve_ivp(f3, t_span, y0, t_eval=t_eval)
    sol1a = f1analytic(t_eval, y0[0])
    sol2a = f2analytic(t_eval, y0[0])
    sol3a = f3analytic(t_eval, y0[0])

    plot(sol1.t, sol1.y[0], t_eval, sol1a, "$y' = -0.5y^2t$")
    plot(sol2.t, sol2.y[0], t_eval, sol2a, "$y' = -0.5t$")
    plot(sol3.t, sol3.y[0], t_eval, sol3a, "$y' = t(1+y)$", log=True)


if __name__ == "__main__":
    main()
