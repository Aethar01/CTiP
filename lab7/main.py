#!/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
import scipy.integrate as spi
import scipy.special as sps
import sys
import numpy as np
from matplotlib import cm
from matplotlib import colors


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', type=int,
                        default=1, help='Function number')
    return parser.parse_args()


def f1(x):
    a = np.sin(13/3 * np.pi * x) ** 3
    b = 2 * np.cos(2 * np.cos(x/np.pi) ** 3) ** 2
    return abs(a-b)


def f2(x, y):
    return x ** 2 + 2 * y ** 2


def f3(x, y):
    return x ** 2 + y ** 2


def f4(x, y, z):
    return np.e ** (x * y * z)


def plot(func, x, y, z=None, w=None, title='', **kwargs):
    if z is not None:
        if w is not None:
            if 'ax' in kwargs:
                ax = kwargs['ax']

                def w_to_color_map(w):
                    norm = colors.Normalize(vmin=np.min(w), vmax=np.max(w))
                    return cm.cool(norm(w))

                wcolors = [w_to_color_map(i) for i in w]

                ax.plot_surface(x, y, z, linewidth=0.2,
                                antialiased=True, cmap='cool', facecolors=wcolors, alpha=0.5)
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')
                ax.set_title(title)
                plt.savefig(f'plots/{title.strip("$\\").replace('/', '')}.png')
                plt.show()
                return
        if 'ax' in kwargs:
            ax = kwargs['ax']
            ax.plot_surface(x, y, z, linewidth=0.2,
                            antialiased=True, cmap='summer', alpha=0.5)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.set_title(title)
            plt.savefig(f'plots/{title.strip("$\\ /").replace('/', '')}.png')
            plt.show()
            return
    else:
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(title)
        plt.savefig(f'plots/{title.strip("$\\ /").replace('/', '')}.png')
        plt.show()


def make_points_in_range(func, **kwargs):
    if 'range_x' in kwargs:
        x = np.linspace(kwargs['range_x'][0], kwargs['range_x'][1], 200)
        y = func(x)
        return x, y
    elif 'range_xy' in kwargs:
        x = np.linspace(kwargs['range_xy'][0], kwargs['range_xy'][1], 200)
        y = np.linspace(kwargs['range_xy'][2], kwargs['range_xy'][3], 200)
        x, y = np.meshgrid(x, y)
        z = func(x, y)
        return x, y, z
    elif 'range_xyz' in kwargs:
        x = np.linspace(kwargs['range_xyz'][0], kwargs['range_xyz'][1], 200)
        y = np.linspace(kwargs['range_xyz'][2], kwargs['range_xyz'][3], 200)
        z = np.linspace(kwargs['range_xyz'][4], kwargs['range_xyz'][5], 200)
        x, y = np.meshgrid(x, y)
        z = x * y
        w = func(x, y, z)
        return x, y, z, w
    else:
        raise ValueError('Invalid range')
    # x = np.linspace(range_x[0], range_x[1], 200)
    # y = func(x)
    # return x, y


def montecarlo_integration(func, x, y, n):
    area = 0
    xmin, xmax = x[0], x[-1]
    ymin, ymax = 0, max(y)
    coords = []
    for i in range(n):
        x_rand = np.random.uniform(xmin, xmax)
        y_rand = np.random.uniform(ymin, ymax)
        if y_rand <= func(x_rand):
            area += 1
            coords.append([x_rand, y_rand, 0])
            # plt.plot(x_rand, y_rand, 'ro', markersize=1)
        else:
            coords.append([x_rand, y_rand, 1])
            # plt.plot(x_rand, y_rand, 'bo', markersize=1)

    xin = [x for x, y, c in coords if c == 0]
    yin = [y for x, y, c in coords if c == 0]
    xout = [x for x, y, c in coords if c == 1]
    yout = [y for x, y, c in coords if c == 1]

    plt.scatter(xin, yin, marker='o', color='r', s=1)
    plt.scatter(xout, yout, marker='o', color='b', s=1)

    return area/n * (xmax - xmin) * (ymax - ymin)


def three_d_montercarlo_integration(func, x, y, z, n, ax, **kwargs):
    volume = 0
    xmin, xmax = kwargs['range_xy'][0], kwargs['range_xy'][1]
    ymin, ymax = kwargs['range_xy'][2], kwargs['range_xy'][3]
    zmin, zmax = 0, np.max(z)
    coords = []
    for i in range(n):
        x_rand = np.random.uniform(xmin, xmax)
        y_rand = np.random.uniform(ymin, ymax)
        z_rand = np.random.uniform(zmin, zmax)
        if z_rand <= func(x_rand, y_rand):
            volume += 1
            coords.append([x_rand, y_rand, z_rand, 0])
            # ax.plot(x_rand, y_rand, z_rand, 'ro', markersize=1)
        else:
            coords.append([x_rand, y_rand, z_rand, 1])
            # ax.plot(x_rand, y_rand, z_rand, 'bo', markersize=1)

    xin = [x for x, y, z, c in coords if c == 0]
    yin = [y for x, y, z, c in coords if c == 0]
    zin = [z for x, y, z, c in coords if c == 0]
    xout = [x for x, y, z, c in coords if c == 1]
    yout = [y for x, y, z, c in coords if c == 1]
    zout = [z for x, y, z, c in coords if c == 1]

    scatter = ax.scatter(xin, yin, zin,
                         marker='o', c='r', s=1)
    scatter = ax.scatter(xout, yout, zout,
                         marker='o', c='b', s=1)
    return volume/n * (xmax - xmin) * (ymax - ymin) * (zmax - zmin)


def four_d_montercarlo_integration(func, x, y, z, w, n, ax, **kwargs):
    volume = 0
    xmin, xmax = kwargs['range_xyz'][0], kwargs['range_xyz'][1]
    ymin, ymax = kwargs['range_xyz'][2], kwargs['range_xyz'][3]
    zmin, zmax = kwargs['range_xyz'][4], kwargs['range_xyz'][5]
    wmin, wmax = 0, np.max(w)
    coords = []
    for i in range(n):
        x_rand = np.random.uniform(xmin, xmax)
        y_rand = np.random.uniform(ymin, ymax)
        z_rand = np.random.uniform(zmin, zmax)
        w_rand = np.random.uniform(wmin, wmax)
        if w_rand <= func(x_rand, y_rand, z_rand):
            volume += 1
            coords.append([x_rand, y_rand, z_rand, w_rand, 0])
            # ax.scatter(x_rand, y_rand, z_rand, marker='o',
            #            c=w_rand, cmap='summer', s=1)
        else:
            coords.append([x_rand, y_rand, z_rand, w_rand, 1])

    xin = [x for x, y, z, w, c in coords if c == 0]
    yin = [y for x, y, z, w, c in coords if c == 0]
    zin = [z for x, y, z, w, c in coords if c == 0]
    win = [w for x, y, z, w, c in coords if c == 0]
    xout = [x for x, y, z, w, c in coords if c == 1]
    yout = [y for x, y, z, w, c in coords if c == 1]
    zout = [z for x, y, z, w, c in coords if c == 1]
    wout = [w for x, y, z, w, c in coords if c == 1]

    scatterin = ax.scatter(xin, yin, zin,
                           marker='o', c=win, cmap='cool', s=1)
    scatterout = ax.scatter(xout, yout, zout,
                            marker='x', c=wout, cmap='hot', s=1)
    plt.colorbar(scatterin, label='w in hypervolume')
    plt.colorbar(scatterout, label='w out of hypervolume')
    return volume/n * (xmax - xmin) * (ymax - ymin) * (zmax - zmin) * (wmax - wmin)


def main():
    args = parse_args()
    match args.function:
        case 1:
            f = f1
            n = 10000
            range_x = (2.5, 7.5)
            x, y = make_points_in_range(f, range_x=range_x)
            area = montecarlo_integration(f, x, y, n)
            plot(f, x, y, title=f'P{
                 args.function}, Monte Carlo integration area={area} \n n={n}')
        case 2:
            f = f2
            n = 10000
            range_xy = (0, 1, 0, 4)
            x, y, z = make_points_in_range(f, range_xy=range_xy)
            fig = plt.figure()
            ax = fig.subplots(subplot_kw={"projection": "3d"})
            volume = three_d_montercarlo_integration(
                f, x, y, z, n, ax, range_xy=range_xy)
            plot(f, x, y, z, title=f'P{
                 args.function}, Monte Carlo integration volume={volume} \n Analytical Solution=44 \n n={n}', ax=ax)
        case 3:
            f = f3
            n = 10000
            range_xy = (0, 1, 0, 4)
            x, y, z = make_points_in_range(f, range_xy=range_xy)
            fig = plt.figure()
            ax = fig.subplots(subplot_kw={"projection": "3d"})
            volume = three_d_montercarlo_integration(
                f, x, y, z, n, ax, range_xy=range_xy)
            plot(f, x, y, z, title=f'P{
                 args.function}, Monte Carlo integration volume={volume} \n Analytical Solution=64/9=7.1111 \n n={n}', ax=ax)
        case 4:
            f = f4
            n = 10000
            range_xyz = (0, 1, 0, 1, 0, 1)
            x, y, z, w = make_points_in_range(f, range_xyz=range_xyz)
            fig = plt.figure()
            ax = fig.subplots(subplot_kw={"projection": "3d"})
            hyper_volume = four_d_montercarlo_integration(
                f, x, y, z, w, n, ax, range_xyz=range_xyz)
            plot(f, x, y, z, w, title=f'P{
                 args.function}, Monte Carlo integration hypervolume={hyper_volume} \n Analytical Solution=$_{3}F_{3}(1,1,1; 2,2,2; 1) \\approx 1.1465$ \n n={n}', ax=ax)
        case _:
            raise ValueError('Invalid function number')
            sys.exit(1)


if __name__ == '__main__':
    main()
