#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def f(x: np.ndarray) -> np.ndarray:
    if isinstance(x, np.ndarray):
        x = x[(x >= 0) & (x <= 4)]
    return np.cos(np.log(x-1)/np.log(x))


def plot(x: np.ndarray, y: np.ndarray, title: str):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    plt.savefig('plots/P2/f.png')
    plt.show()


def main():
    x = np.linspace(0, 4, 10000)
    y = f(x)
    plot(x, y, 'f(x) = cos(log(x-1)/log(x)); [0, 4]')


if __name__ == '__main__':
    main()
    print(f(1.46))
    print(f(1.16))
