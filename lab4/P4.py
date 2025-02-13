#!/usr/bin/env python3

# animated matplotlib random walk
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
import matplotlib.animation as animation
import sys


def main(animate: bool = True, threed: bool = False):
    # initializing plot
    fig = plt.figure()

    fig.suptitle(
        'Random walk with step of 1')

    fig.subplots_adjust(hspace=.4)

    # defining the board

    if threed:
        board = fig.add_subplot(1, 1, 1, projection='3d')
    else:
        board = fig.add_subplot(1, 1, 1)

    # defining the data frame
    if threed:
        dataframe = pd.DataFrame(
            {'x_point': [], 'y_point': [], 'z_point': [], 'x_end_point': [], 'y_end_point': [], 'z_end_point': []})
        dataframe.loc[0] = [0, 0, 0, 0, 0, 0]
    else:
        dataframe = pd.DataFrame(
            {'x_point': [], 'y_point': [], 'x_end_point': [], 'y_end_point': []})
        dataframe.loc[0] = [0, 0, 0, 0]

    if animate:
        def update(frame):
            # establishing the first point and the angle
            x = dataframe['x_end_point'].iloc[-1]
            y = dataframe['y_end_point'].iloc[-1]
            if threed:
                z = dataframe['z_end_point'].iloc[-1]
            theta = np.pi*rd.uniform(0, 2)

            # defining end point

            x_end = x + np.sin(theta)
            y_end = y + np.cos(theta)
            if threed:
                z_end = z + np.cos(theta)

            if threed:
                dataframe.loc[dataframe.index.max() + 1] = [
                    x, y, z, x_end, y_end, z_end]
            else: 
                dataframe.loc[dataframe.index.max() + 1] = [x, y, x_end, y_end]

            if threed:
                board.plot([x, x_end], [y, y_end], [z, z_end])
            else:
                board.plot([x, x_end], [y, y_end])

        ani = animation.FuncAnimation(
            fig, update, frames=100, repeat=False, blit=True)
        ani.save('random_walk.gif', writer='imagemagick')
        plt.show()

    else:
        for n in range(0, 100):
            # establishing the first point and the angle
            x = dataframe['x_end_point'].iloc[-1]
            y = dataframe['y_end_point'].iloc[-1]
            if threed:
                z = dataframe['z_end_point'].iloc[-1]
            theta = np.pi*rd.uniform(0, 2)

            # defining end point

            x_end = x + np.sin(theta)
            y_end = y + np.cos(theta)
            if threed:
                z_end = z + np.cos(theta)

            if threed:
                dataframe.loc[dataframe.index.max() + 1] = [
                    x, y, z, x_end, y_end, z_end]
            else:
                dataframe.loc[dataframe.index.max() + 1] = [x, y, x_end, y_end]

            if threed:
                board.plot([x, x_end], [y, y_end], [z, z_end])
            else:
                board.plot([x, x_end], [y, y_end])

        plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        animate = False
        threed = False
        for arg in sys.argv[1:]:
            if arg == '-a':
                animate = True
            elif arg == '-3':
                threed = True
            else:
                print(f'Unknown argument: {arg}')
                sys.exit(1)
        main(animate=animate, threed=threed)
    else:
        main(animate=False, threed=False)
