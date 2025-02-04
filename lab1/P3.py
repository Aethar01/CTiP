#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from math import e, pi


def f1(x):
    return np.cos(x)


def f2(x):
    return np.cos(x) * np.cos(x) - np.sin(x)


def f3(x):
    return np.exp(x) - 10 ** x


def f4(x):
    return np.emath.logn(e, x) - e ** x + 10


def area_bound(x, y):
    area_lowerbound = round(abs(max(x)-min(x)) * abs(y[0] - min(y)), 4)
    area_upperbound = round(abs(max(x)-min(x)) * abs(max(y) - min(y)), 4)
    return area_lowerbound, area_upperbound


def plot_with_bounds(func, title, bounds):
    x = np.linspace(bounds[0], bounds[1], 1000)
    y = func(x)
    bound1 = bounds[0]
    bound2 = bounds[1]
    plt.plot(x, y, label=title)
    plt.plot([bound1, bound1], [min(y), max(y)], linestyle='--', color='red')
    plt.plot([bound2, bound2], [min(y), max(y)], linestyle='--', color='red')
    plt.plot([min(x), max(x)], [max(y), max(y)],
             linestyle='--', color='green')
    plt.plot([min(x), max(x)], [min(y), min(y)],
             linestyle='--', color='green')
    plt.plot([min(x), max(x)], [y[0], y[0]], linestyle='--', color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    area_lowerbound, area_upperbound = area_bound(x, y)
    title += f'\n Area upperbound: {
        area_upperbound}\n Area lowerbound: {area_lowerbound}'
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.minorticks_on()
    plt.savefig(f"plots/P3/{title}.png")
    plt.show()


def plot_for_last_func(func, title):
    x = np.linspace(0, 3, 1000)
    y = func(x)
    y = y[y > 0]
    x = x[x > 0]
    x = x[:len(y)]
    plt.plot(x, y, label=title)
    plt.plot([min(x), min(x)], [min(y), max(y)], linestyle='--', color='red')
    plt.plot([max(x), max(x)], [0, max(y)], linestyle='--', color='red')
    plt.plot([min(x), max(x)], [max(y), max(y)],
             linestyle='--', color='green')
    plt.plot([min(x), max(x)], [min(y), min(y)],
             linestyle='--', color='green')
    plt.plot([min(x), max(x)], [y[0], y[0]], linestyle='--', color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    area_lowerbound, area_upperbound = area_bound(x, y)
    title += f'\n Area upperbound: {
        area_upperbound}\n Area lowerbound: {area_lowerbound}'
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.minorticks_on()
    plt.savefig(f"plots/P3/{title}.png")
    plt.show()


def main():
    plot_with_bounds(f1, 'f(x) = cos(x), [-pi, pi]', [-pi, pi])
    plot_with_bounds(f2, 'f(x) = cos(x)^2 - sin(x), [-pi, pi*0.5]', [-pi, pi/2])
    plot_with_bounds(f3, 'f(x) = exp(x) - 10^x, [-10, 0]', [-10, 0])
    plot_for_last_func(f4, 'f(x) = log(x) - e^x + 10, x > 0, f(x) > 0')


if __name__ == "__main__":
    main()
