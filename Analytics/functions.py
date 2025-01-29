# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def combined_table(X, Y, x, y):
    x = x.reshape(1, -1)
    y = y.reshape(-1, 1)
    x = np.repeat(x, y.shape[0], axis = 0)
    y = np.repeat(y, x.shape[1], axis = 1)
    df = pd.DataFrame({X: np.ndarray.flatten(x), Y: np.ndarray.flatten(y)})
    return df

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
    
