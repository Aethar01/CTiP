#!/usr/bin/env python3

# y <= (120 - x) / 2
# y >= 60 - x
# y >= x / 2
# y >= (x - 50)^2
# x, y >= 0

import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return (120 - x) / 2


def f2(x):
    return 60 - x


def f3(x):
    return x / 2


def f4(x):
    return (x - 50) ** 2


def plot(func, x, title):
    y = func(x)
    x = x[y >= 0]
    y = y[y >= 0]
    plt.plot(x, y, label=title)
    return x, y


def plot_all():
    x = np.linspace(40, 60, 1000)
    x1, y1 = plot(f1, x, 'y <= (120 - x) / 2')
    x2, y2 = plot(f2, x, 'y >= 60 - x')
    x3, y3 = plot(f3, x, 'y >= x / 2')
    x4, y4 = plot(f4, x, 'y >= (x - 50)^2')
    # fill between the curves as specified
    plt.fill_between(x1, y1, y2, color='gray', alpha=0.5)
    plt.fill_between(x1, y1, y3, color='gray', alpha=0.5)
    plt.fill_between(x1, y1, y4, color='gray', alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.title('Inequalities where the darkest shaded region is the feasible region')
    plt.minorticks_on()
    plt.savefig('plots/P4/inequalities.png')
    plt.show()


def main():
    plot_all()


if __name__ == '__main__':
    main()
