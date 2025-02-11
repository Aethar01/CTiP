#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def f(a: float, b: float, c: float) -> tuple[float]:
    x1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
    return (x1, x2)


def falter(a: float, b: float, c: float) -> tuple[float]:
    x1 = -2*c / (b + np.sqrt(b**2 - 4*a*c))
    x2 = -2*c / (b - np.sqrt(b**2 - 4*a*c))
    return (x1, x2)


def solve(a: float, b: float, c: float) -> list[float]:
    x = sp.symbols('x')
    eq = a*x**2 + b*x + c
    return sp.solve(eq, x)


def plot(a: float, b: float, c: float) -> None:
    fig, ax = plt.subplots()
    x = np.linspace(-1001000, 1000, 1000)
    y = 0.001*x**2 + 1000*x - 0.001
    ax.plot(x, y)
    axins1 = ax.inset_axes([0.15, 0.6, 0.3, 0.3], xlim=(-1.05e6, -0.95e6), ylim=(-1, 1))
    axins2 = ax.inset_axes([0.6, 0.6, 0.3, 0.3], xlim=(-1, 1), ylim=(-1, 1))
    axins1.plot(x, y)
    axins2.plot(x, y)
    ax.indicate_inset_zoom(axins1, edgecolor="black")
    ax.indicate_inset_zoom(axins2, edgecolor="black")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    coefficients = (0.001, 1000, -0.001)
    plot(*coefficients)
    print("regular", f(*coefficients))
    print("alternate", falter(*coefficients))
    print("sympy", solve(*coefficients))
