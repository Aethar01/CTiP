#!/usr/bin/env python3

import numpy as np


def f(x: np.ndarray) -> np.ndarray:
    '''
    evaluating the function with large x means that 1 << x so the demoninator is approximately 0 and will evaluate to infinity/undefined.
    '''
    y = np.sqrt(x**2 + 1) + x
    return y


def plot(x: np.ndarray, y: np.ndarray) -> None:
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    x = np.array([0, 1e8])
    y = f(x)
    print(y)
    x1 = np.linspace(0, 1e8, 100000)
    y1 = f(x1)
    plot(x1, y1)
