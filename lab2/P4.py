#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def plot(x: np.ndarray, y: np.ndarray, title: str):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    title = title.strip().replace(' ', '_').replace('/', '_')
    plt.savefig(f'plots/P4/{title}.png', bbox_inches='tight')
    plt.show()


def f1(x: np.ndarray, n: int) -> np.ndarray:
    if isinstance(x, np.ndarray):
        x = x[(x >= 0) & (x <= 4*np.pi)]
    y = np.zeros(x.shape)
    for i in range(1, n+1):
        y += 1/(2*i-1)**2 * np.cos((2*i-1)*x)
    return y


def increasing_n(max_n: int, func, title: str, flag: bool = False):
    x = np.linspace(0, 4*np.pi, 10000)
    for i in range(1, max_n+1):
        y = func(x, i)
        if flag:
            plot(x, y, title)


def residual(max_n: int, func, title: str, flag: bool = False):
    x = np.linspace(0, 4*np.pi, 10000)
    for j in range(1, max_n+1):
        y = func(x, j+1) - f1(x, j)
        if flag:
            plot(x, y, f'Residual for n = {j}')


def main():
    n = 4
    increasing_n(
        n, f1, f'f(x) = Σ cos((2n-1)x)/(2n-1)^2; [0, 4π] for n = {n}', True)
    residual(
        n, f1, f'f(x) = Σ cos((2n-1)x)/(2n-1)^2; [0, 4π] for n = {n}', True)


if __name__ == '__main__':
    main()
