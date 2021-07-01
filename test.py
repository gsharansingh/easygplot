import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


data = pd.read_csv("gasprices.csv")

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
data.iloc[:, 1:] = imputer.fit_transform(data.iloc[:, 1:])
print(data.head())

import easygplot
easygplot.plot(data.iloc[:, 0], data.iloc[:, 1:], title = "Gas Prices", legend = list(data.columns[1:]))

from easygplot import plot_csv, read
mydata = read.CSV("gasprices.csv")
print(mydata[:, 0])
print(mydata)
print(len(mydata))

# print([data for data in mydata])

plot_csv.plot_csv("gasprices.csv", x_column = 0, row_label = "Years", column_label = "Countries", title = "Gas Prices", legend=True, linestyle = "solid", other_graphs=['all'])