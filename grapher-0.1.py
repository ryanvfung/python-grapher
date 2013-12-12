# -*- coding: utf-8 -*-
""" Quick Grapher 0.1
    @author: Ryan Fung
    Create Date: 2013-11-28
"""
print("\n===== Quick Grapher 0.1 by Ryan Fung =====\n")
import numpy
import matplotlib.pyplot as plt


def grapher(function, a, b, iterations=101):
    """Graphs 'function' from x='a' to x='b' using 'iterations' number of
    iterations, shows the graph plot and returns None."""
    xs = numpy.linspace(a, b, iterations)
    ys = [function(x) for x in xs]
    plt.plot(xs, ys)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

function = input("Input function:\n>>>")
a = input("Input lower bound:\n>>>")
b = input("Input upper bound:\n>>>")
iterations = input("Input number of iterations (0 for default):\n>>>")
if iterations == 0:
    grapher(function, a, b)
else:
    grapher(function, a, b, iterations)
