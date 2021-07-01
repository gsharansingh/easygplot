import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.impute import SimpleImputer
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class CSV:
    def __init__ (self, filename, labels = True, delimiter=","):
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
        
    # def __call__(self, index = None):
    #     if index == None:
    #         print(self.csv_data.describe())
    #     else:
    #         print(self.columns[index], self.csv_data.iloc[:, index])

    def __getitem__ (self, index):
        return self.data[index]

    def __str__ (self):
        return f"Columns: {self.columns}"

    def __len__ (self):
        return self.data.shape[0]