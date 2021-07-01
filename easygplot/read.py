import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.impute import SimpleImputer
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class CSV:
    def __init__ (self, filename, labels = True, delimiter=",", x_axis_label = True):
        self.data = None
        self.columns = []
        try:
            with open(filename, 'r') as csvfile:
                # creating a csv reader object
                csvreader = csv.reader(csvfile, delimiter=delimiter)

                # extracting field names through first row
                if labels:
                    self.columns = next(csvreader)
                
                self.data = np.genfromtxt(csvfile, delimiter=delimiter)
            
        except:
            raise "Give a valid filename!!"

        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
        self.data[:, 1:] = imputer.fit_transform(self.data[:, 1:])

        if x_axis_label == False:
            columns_label = list(range(rows.shape[0]))
            self.row_data = self.data[:, 0:]
        else:
            columns_label = self.data[:, 0]
            self.row_data = self.data[:, 1:]

        self.labels = (columns_label, self.columns[1:])
            
    # def __call__(self, index = None):
    #     if index == None:
    #         print(self.csv_data.describe())
    #     else:
    #         print(self.columns[index], self.csv_data.iloc[:, index])

    def __getitem__ (self, index):
        return self.row_data[index], self.labels

    def __str__ (self):
        return f"Columns: {self.columns}"

    def __len__ (self):
        return self.data.shape[0]