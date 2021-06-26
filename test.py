import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


data = pd.read_csv("gasprices.csv")
print(data.columns)

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
data.iloc[:, 1:] = imputer.fit_transform(data.iloc[:, 1:])

import easygplot
easygplot.plot(data['Year'], data.iloc[:,1:], title = "Gas Prices", legend = list(data.columns[1:]))