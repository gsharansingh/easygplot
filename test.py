import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


data = pd.read_csv("gasprices.csv")

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
data.iloc[:, 1:] = imputer.fit_transform(data.iloc[:, 1:])
print(data.head())

import easygplot
easygplot.plot(data.iloc[:, 0], data.iloc[:, 1:], title = "Gas Prices", legend = list(data.columns[1:]))

from easygplot import plot_csv, read, Plot
mydata = read.CSV("gasprices.csv")
# print(mydata[:])
# print(mydata)
# print(len(mydata))

line_plot = Plot.Line(legend=True)
line_plot(mydata[:])
# l1, l2 = mydata[3]
# print(l2[1])
Plot.Line(legend=True)(mydata[1])

# print([data for data in mydata])
from torchvision import transforms
plot_obj = transforms.Compose([Plot.Line(legend=True), Plot.Bar(legend=True), Plot.Box(), Plot.Histogram(legend=True), Plot.Pie(legend=True)])
a = plot_obj(mydata[:])
# plot_csv.plot_csv("gasprices.csv", x_column = 0, row_label = "Years", column_label = "Countries", title = "Gas Prices", legend=True, linestyle = "solid", other_graphs=['all'])