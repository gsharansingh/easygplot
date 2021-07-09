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
        Set 'True', if you want to set any column in the file as x-axis. 
        Set 'False', if you want indexing of x-axis from 0 to length(rows).
    delimiter: one char str (default = `,`)
        If the csv file is separated with some other symbols (such as ':', ';', '/t',....), Input that symbol.
    set_index: int (default = 0)
        If you want some other column index to be x-axis, pass that column index. 
        If you do not want any column index to be x-axis, pass 'None'.
    missing_data_handling_strategy: str, Optional (default = 'mean')
        In the case, some values are missing in the file, then either replace the values or drop the row/column.
        If 'mean', it will replace missing value using mean along column.
        If 'median', it will replace missing value using median along column.
        If 'most_frequent', it will replace missing value using the most frequent value along column.
        If 'constant', it will replace missing value with fill_value.
        If 'drop_row', it will drop the whole row containing missing value.
        If 'drop_column', it will drop the whole column containing missing value.
    skip_lines: int (default = None)
        If some empty line(s) or description present in the beginning of the file,
        input the number of lines to discard the lines. 
    TODO:
        Complete
    """
    def __init__ (self, filename, labels = True, delimiter=",", set_index = 0, missing_data_handling_strategy = 'mean', skip_lines = None):
        
        self.data = None
        self.columns = []
        try:
            with open(filename, 'r') as csvfile:
                # creating a csv reader object
                csvreader = csv.reader(csvfile, delimiter=delimiter)
                if skip_lines:
                    for _ in range(skip_lines):
                        next(csvreader)

                # extracting field names through first row
                if labels:
                    self.columns = next(csvreader)
                
                self.data = np.genfromtxt(csvfile, delimiter=delimiter)
            
        except:
            raise "Give a valid filename!!"

        if np.isnan(self.data).any():
            import matplotlib.pyplot as plt
            print("Data contains missing values. Here is the representation of missing values:")
            plt.imshow(~np.isnan(self.data), aspect = 'auto', cmap = plt.cm.gray, interpolation='nearest')
            self.data = np.delete(self.data, np.argwhere(np.isnan(self.data).all(axis = 0)), axis = 1)
            self.data = np.delete(self.data, np.argwhere(np.isnan(self.data).all(axis = 1)), axis = 0)
            print("""NOTE: if the data has whole row or column as missing values, that row or column is already dropped!\
            \nFor more information, check 'missing_data_handling_strategy' parameter in Docu String by: 'print(easygplot.read.CSV.__doc__)'""")

        if missing_data_handling_strategy == 'drop_column':
            self.data = np.delete(self.data, np.argwhere(np.isnan(self.data).any(axis = 0)), axis = 1)
        elif missing_data_handling_strategy == 'drop_row':
            self.data = np.delete(self.data, np.argwhere(np.isnan(self.data).any(axis = 1)), axis = 0)
        else:
            imputer = SimpleImputer(missing_values=np.nan, strategy=missing_data_handling_strategy)
            self.data[:, :] = imputer.fit_transform(self.data[:, :])

        if set_index == None:
            self.x_label = list(range(self.data.shape[0]))
            self.row_data = self.data[:, :]
            if labels:
                self.labels = (self.x_label, self.columns)
            else:
                self.labels = (self.x_label, list(range(self.data.shape[1])))
        else:
            self.x_label = self.data[:, set_index]
            if set_index == 0:
                self.row_data = self.data[:, 1:]
                if labels:
                    self.labels = (self.x_label, self.columns[1:])
                else:
                    self.labels = (self.x_label, list(range(self.data.shape[1]-1)))
            else:
                self.row_data = np.hstack((self.data[:, :set_index], self.data[:, set_index+1:]))
                if labels:
                    self.labels = (self.x_label, self.columns[:set_index] + (self.columns[set_index+1:]))
                else:
                    self.labels = (self.x_label, list(range(self.data.shape[1]-1)))

    def __getitem__ (self, index):
        
        return self.row_data[:, index], (self.labels[0], self.labels[1][index])


    def __str__ (self):
        return f"Columns: {self.columns}"


    def __len__ (self):
        return self.data.shape[0]