import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

def plot_csv(filename, x_columns = [0], y_columns = [1], legend=False):
    try:
        data = pd.read_csv(filename)
    except:
        raise "Give a valid filename!!"

    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    data.iloc[:, 1:] = imputer.fit_transform(data.iloc[:, 1:])

    plt.plot(data.iloc[:, 0], data.iloc[:, 1:])
    # if title:
    #     plt.title(title)
    # if xlabel:
    #     plt.xlabel(xlabel)
    # if ylabel:
    #     plt.ylabel(ylabel)
    if legend:
        plt.legend(list(data.columns[1:]))
    plt.show()