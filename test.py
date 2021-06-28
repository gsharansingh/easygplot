import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


data = pd.read_csv("gasprices.csv")
print(data.columns)

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
data.iloc[:, 1:] = imputer.fit_transform(data.iloc[:, 1:])

import easygplot
easygplot.plot(data.iloc[:, 0], data.iloc[:, 1:], title = "Gas Prices", legend = list(data.columns[1:]))

from easygplot import plot_csv
plot_csv.plot_csv("gasprices.csv", x_column = 0, title = "Gas Prices", legend=True, linestyle = "solid", other_graphs=['pie'])