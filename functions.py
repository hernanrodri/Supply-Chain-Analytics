# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator

def combined_table(X, Y, x, y):
    x = x.reshape(1, -1)
    y = y.reshape(-1, 1)
    x = np.repeat(x, y.shape[0], axis = 0)
    y = np.repeat(y, x.shape[1], axis = 1)
    df = pd.DataFrame({X: np.ndarray.flatten(x), Y: np.ndarray.flatten(y)})
    return df

def constraint(df, operators, variables):
    table = {"<=": operator.le, ">=": operator.ge, "==": operator.eq, "sum": np.sum, "mean": np.mean, "min": np.min, "max": np.max} #lookup table
    operation1 = table[operators[0]]
    operation2 = table[operators[1]]
    operation3 = table[operators[2]]
    v = variables[-2]
    w = variables[-1]
    func = lambda x: {v: operation1(x, axis = 0), w: operation3(x, axis = 0)}[x.name]
    g = df.groupby(by = variables[:-2]).transform(func)
    g[v] = np.where(operation2(g[v], g[w]), g[v], g[w])
    return g

def plot_scatter(X, Y, x, y):
    plt.style.use("seaborn-darkgrid")
    plt.figure(figsize = (9, 7))
    plt.scatter(x, y, s = 5)
    plt.xlabel(X)
    plt.ylabel(Y)
    plt.show()

def plot_bar(X, Y, x, y):
    plt.style.use("seaborn-darkgrid")
    plt.figure(figsize = (9, 7))
    plt.bar(x, height = y)
    plt.xlabel(X)
    plt.xticks(x)
    plt.ylabel(Y)
    plt.show()
    
def plot_hist(X, Y, x, bins):
    plt.style.use("seaborn-darkgrid")
    plt.figure(figsize = (9, 7))
    plt.hist(x, bins)
    plt.xlabel(X)
    plt.ylabel(Y)
    plt.show()
    
def plot_pie(title, x, y, format_value):
    plt.style.use("seaborn-darkgrid")
    plt.figure(figsize = (9, 7))
    plt.title(title)
    plt.pie(x, labels = y, autopct = format_value)
    plt.show()
    
