import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.impute import SimpleImputer
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class CSV:
    """
    This module will read the csv file and create an object containing data and labels.
    Parameters
    ----------
    filename: str
        Input the name of the csv file to read.
        For example, Plot.CSV('...filename.csv...')
    labels: bool (default = True)
        Set 'True', if the first row of the csv file is columns.
        Set 'False', if the first row of the csv file is not columns.
    delimiter: one char str (default = `,`)
        If the csv file is separated with some other symbols (such as ':', ';', '/t',....), Input that symbol.
    x_axis_column: int (default = 0)
        If you want some other column index to be x-axis, pass that column index. 
        If you do not want any column index to be x-axis, pass 'None'.
    missing_data_handling_strategy: str, Optional (default = 'mean')
        In the case, some values are missing in the file.
        We can `Drop` those rows or use some other strategy to handle the data.
        Default, it is `mean`

    TODO:
        1. Implement the y-axis data selection
        2. Implement the self.labels in the case the first row of csv file does not contains labels,
        i.e. if `labels == False`
        3. 
    """
    def __init__ (self, filename, labels = True, delimiter=",", x_axis_column = 0, missing_data_handling_strategy = 'mean'):
        
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

        imputer = SimpleImputer(missing_values=np.nan, strategy=missing_data_handling_strategy)
        self.data[:, 1:] = imputer.fit_transform(self.data[:, 1:])

        if x_axis_column == None:
            self.x_label = list(range(self.data.shape[0]))
            self.row_data = self.data[:, 0:]
        else:
            self.x_label = self.data[:, x_axis_column]
            self.row_data = self.data[:, 1:]

        self.labels = (self.x_label, self.columns[1:])


    def __getitem__ (self, index):
        
        return self.row_data[:, index], (self.labels[0], self.labels[1][index])


    def __str__ (self):
        return f"Columns: {self.columns}"


    def __len__ (self):
        return self.data.shape[0]