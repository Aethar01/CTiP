#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def gen_data(n=10000):
    return np.random.rand(n, 2)


def plot_data(data):
    fig, ax = plt.subplots()
    inside = data[np.sqrt(data[:, 0]**2 + data[:, 1]**2) < 1]
    ratio = len(inside) / len(data)
    print(f'Ratio: {ratio}')
    print(f'Pi estimate: {ratio * 4}')
    ax.scatter(data[:, 0], data[:, 1], color='red', s=0.5)
    ax.scatter(inside[:, 0], inside[:, 1], color='blue', s=0.5)
    ax.set_aspect('equal')
    plt.show()


def main():
    data = gen_data(10**6)
    plot_data(data)


if __name__ == '__main__':
    main()
