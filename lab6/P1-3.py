#!/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
import scipy.integrate as spi
import scipy.special as sps
import numpy as np
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', type=int,
                        default=1, help='Function number')
    return parser.parse_args()


def f1(x):
    return 1/(1+x**2)


def f2(x):
    return 1/x


def f3(x):
    return np.sin(x**2)


def make_points_in_range(func, range_x: range):
    x = np.linspace(range_x[0], range_x[1], 100)
    y = func(x)
    return x, y


def plot(func, x, y, title):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.savefig(f'plots/P1-3_{title.strip("$\\")}.png')
    plt.show()


def integrate(intgrationmethod, func, x, y):
    match intgrationmethod:
        case 'quad':
            return spi.quad(func, x[0], x[-1])
        case 'trapezoid':
            return spi.trapezoid(y, x)
        case 'simpson':
            return spi.simpson(y, x)
        case 'gauss':
            return spi.fixed_quad(func, x[0], x[-1])
        case _:
            return None


def plot_and_integrate(func, xrange, title, analytical_result=None):
    x, y = make_points_in_range(func, xrange)
    plot(func, x, y, title)
    print(f'analytical: {analytical_result}')
    quad_result = integrate('quad', func, x, y)[0]
    print(f'quad: {quad_result}, residual: {
          abs(quad_result - analytical_result)}')
    trapezoid_result = integrate('trapezoid', func, x, y)
    print(f'trapezoid: {trapezoid_result}, residual: {
          abs(trapezoid_result - analytical_result)}')
    simpson_result = integrate('simpson', func, x, y)
    print(f'simpson: {simpson_result}, residual: {
          abs(simpson_result - analytical_result)}')
    gauss_result = integrate('gauss', func, x, y)[0]
    print(f'gauss: {gauss_result}, residual: {
          abs(gauss_result - analytical_result)}')


def main():
    args = parse_args()
    match args.function:
        case 1:
            func = f1
            xrange = [0, 5]
            title = '$\\frac{1}{1+x^2}$'
            analytical_result = np.arctan(5)
        case 2:
            func = f2
            xrange = [1, 2]
            title = '$\\frac{1}{x}$'
            analytical_result = np.log(2)
        case 3:
            func = f3
            xrange = [0, 1]
            title = '$\\sin(x^2)$'
            analytical_result = np.sqrt(
                np.pi/2) * sps.fresnel(np.sqrt(2/np.pi))[0]
        case _:
            raise ValueError('Invalid function number')
            sys.exit(1)
    plot_and_integrate(func, xrange, title, analytical_result)


if __name__ == '__main__':
    main()
