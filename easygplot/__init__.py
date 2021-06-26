import matplotlib.pyplot as plt
import numpy as np

def plot(x, y, title=False, xlabel=False, ylabel=False, legend=False):
    """
    x: Input the x-axis values
    y: Input the y-axis values
    xlabel: Provide the label for x-axis
    ylabel: Provide the label for y-axis
    legend: Provide a list of labels representing y-axis values
    """
    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if legend:
        plt.legend(legend)
    plt.show()