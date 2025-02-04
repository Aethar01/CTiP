#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from sys import platform


def solveequation(equation: tuple):
    return globals()[equation[-1]](equation)


def solvelinear(equation: tuple):
    '''
    returns the x and y values for the equation ax + by = c
    inputs:
        tuple: (a: float, b: float, c: float)
    outputs:
        tuple: (x: ndarray, y: ndarray, title: str)
    '''
    x = np.linspace(-5, 5, 100)
    y = (equation[2] - equation[0] * x) / equation[1]
    title = f"{equation[0]}x + {equation[1]}y = {equation[2]}\n"
    return (x, y, title)


def solveb1(equation: tuple):
    '''
    returns the x and y values for the equation ax^2 + by^2 = c
    inputs:
        tuple: (a: float, b: float, c: float)
    outputs:
        tuple: (x: ndarray, y: ndarray, title: str)
    '''
    x = np.linspace(-5, 5, 100)
    a = equation[0]
    b = equation[1]
    c = equation[2]
    y = np.sqrt((c - a * x**2) / b)
    title = f"{a}x^2 + {b}y^2 = {c}\n"
    return (x, y, title)


def solveb1neg(equation: tuple):
    '''
    returns the x and y values for the equation ax^2 + by^2 = c;
    this is the negative version of solveb1
    inputs:
        tuple: (a: float, b: float, c: float)
    outputs:
        tuple: (x: ndarray, y: ndarray, title: str)
    '''
    x = np.linspace(-5, 5, 100)
    a = equation[0]
    b = equation[1]
    c = equation[2]
    y = -np.sqrt((c - a * x**2) / b)
    title = f"{a}x^2 + {b}y^2 = {c}\n"
    return (x, y, title)


def solveb2(equation: tuple):
    '''
    returns the x and y values for the equation ax^2 + bx + cy = d
    inputs:
        tuple: (a: float, b: float, c: float, d: float)
    outputs:
        tuple: (x: ndarray, y: ndarray, title: str)
    '''
    x = np.linspace(-5, 5, 100)
    a = equation[0]
    b = equation[1]
    c = equation[2]
    d = equation[3]
    y = (d - a * x**2 - b * x) / c
    title = f"{a}x^2 + {b}x + {c}y = {d}\n"
    return (x, y, title)


def solvea2(equation: tuple):
    '''
    returns the x and y values for the equation ax^2 + by = c
    inputs:
        tuple: (a: float, b: float, c: float)
    outputs:
        tuple: (x: ndarray, y: ndarray, title: str)
    '''
    x = np.linspace(-5, 5, 100)
    a = equation[0]
    b = equation[1]
    c = equation[2]
    y = (c - a * x**2) / b
    title = f"{a}x^2 + {b}y = {c}\n"
    return (x, y, title)


def solvec1(equation: tuple):
    '''
    returns the x and y values for the equation y = log_2(x + a)
    inputs:
        tuple: (a: float)
    outputs:
        tuple: (x: ndarray, y: ndarray, title: str)
    '''
    x = np.linspace(-5, 5, 100)
    a = equation[0]
    y = np.log2(x + a)
    title = f"y = log_2(x + {a})\n"
    return (x, y, title)


def solvec2(equation: tuple):
    '''
    returns the x and y values for the equation y = a - x
    inputs:
        tuple: (a: float)
    outputs:
        tuple: (x: ndarray, y: ndarray, title: str)
    '''
    x = np.linspace(-5, 5, 100)
    a = equation[0]
    y = a - x
    title = f"y = {a} - x\n"
    return (x, y, title)


def plotlines(equations: list):
    if platform == "linux":
        plt.switch_backend("gtk4agg")
    plottitle = ""
    for equation in equations:
        solved = solveequation(equation)
        x = solved[0]
        y = solved[1]
        title = solved[2]
        plt.plot(x, y, label=f"{title.strip()}")
        plottitle += f"{title}\n"
    plottitle = "".join(plottitle.rsplit("\n", 1))
    plt.title(plottitle)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.minorticks_on()
    plt.legend()
    title = plottitle.strip().replace(" ", "").replace("\n", "_")
    plt.savefig(f"plots/P1-2/{title}.png", bbox_inches='tight')
    plt.show()


def main():
    equations = [(2, 2, 1, "solvelinear"), (3, -2, 0, "solvelinear")]
    equationsP2A = [(1, 1, 1, "solvelinear"), (1, -1, 0, -5, "solvea2")]
    equationsP2B = [(1, 1, 9, "solveb1"), (-1, -3, 1, 1,
                                           "solveb2"), (1, 1, 9, "solveb1neg")]
    equationsP3 = [(4, "solvec1"), (3, "solvec2")]
    plotlines(equations)
    plotlines(equationsP2A)
    plotlines(equationsP2B)
    plotlines(equationsP3)


if __name__ == "__main__":
    main()
