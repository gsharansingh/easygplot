import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.impute import SimpleImputer

def plot_csv(filename, x_column = None, y_column = 1, legend=False, linestyle = 'solid'):
    try:
        # initializing the titles and rows list
        fields = []

        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile, delimiter=",")

            # extracting field names through first row
            fields = next(csvreader)
            
            rows = np.genfromtxt(csvfile, delimiter=",")
            
    except:
        raise "Give a valid filename!!"

    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    rows[:, 1:] = imputer.fit_transform(rows[:, 1:])
    if x_column == None:
        plt.plot(range(rows.shape[0]), rows[:, 0:])
    else:
        plt.plot(rows[:, 0], rows[:, 1:], linestyle = linestyle)
    # if title:
    #     plt.title(title)
    if x_column:
        plt.xlabel(fields[x_column])
    if legend:
        plt.ylabel("Price")
    if legend:
        plt.legend(fields[1:], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
    plt.show()