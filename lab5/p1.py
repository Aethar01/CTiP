#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt
import numpy as np


def generate_uniformly_distributed_cube_points(n):
    points = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)
        points.append([x, y, z])
    return points


def generate_uniformly_distributed_sphere_points(n, onSurface=False):
    points = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)
        if x**2 + y**2 + z**2 <= 1:
            points.append([x, y, z])

    if onSurface:
        for point in points:
            norm = np.linalg.norm(point)
            point[0] /= norm
            point[1] /= norm
            point[2] /= norm
    return points


def generate_uniformly_distributed_circle_points(n, onSurface=False):
    points = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points.append([x, y])

    if onSurface:
        for point in points:
            norm = np.linalg.norm(point)
            point[0] /= norm
            point[1] /= norm
    return points


def plot_points3d(points, title):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    for point in points:
        ax.scatter(point[0], point[1], point[2], c='b', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title(title)
    plt.savefig(f"plots/P1/{title}.png")


def plot_points2d(points, title):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    for point in points:
        ax.scatter(point[0], point[1], c='b', marker='o')
    plt.title(title)
    plt.savefig(f"plots/P1/{title}.png")


def plot_2set_points2d(points, title):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    # only plot z = 0 and z = 0.5
    points1 = [point for point in points if point[2] >= -0.1 and point[2] <= 0.1]
    points2 = [point for point in points if point[2] >= 0.4 and point[2] <= 0.6]

    ax.scatter([point[0] for point in points1], [point[1] for point in points1], c='b', marker='o', label=f"z = 0")
    ax.scatter([point[0] for point in points2], [point[1] for point in points2], c='r', marker='o', label=f"z = 0.5")
    plt.legend()
    plt.title(title)
    plt.savefig(f"plots/P1/{title}.png")


def main():
    n = 1000
    points = generate_uniformly_distributed_cube_points(n)
    plot_points3d(points, "Random points in a cube")
    plot_points2d(points, "Random points in a square")
    points = generate_uniformly_distributed_sphere_points(n)
    plot_points3d(points, "Random points in a sphere")
    plot_points2d(points, "Random points in a circle")
    points = generate_uniformly_distributed_sphere_points(n, onSurface=True)
    plot_points3d(points, "Random points on the surface of a sphere")
    points = generate_uniformly_distributed_circle_points(n, onSurface=True)
    plot_points2d(points, "Random points on the surface of a circle")
    n = 10000
    points = generate_uniformly_distributed_sphere_points(n, onSurface=True)
    plot_2set_points2d(points, "Random points in two circles")


if __name__ == "__main__":
    main()
