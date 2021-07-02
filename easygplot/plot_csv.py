import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
from sklearn.impute import SimpleImputer
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class line(object):
    def __init__ (self, figsize = (8, 5), linestyle = 'solid', legend = False):
        self.figsize = figsize
        self.linestyle = linestyle
        self.legend = legend

    def __call__ (self, sample):
        data, labels = sample
        plt.figure(figsize=self.figsize)
        plt.plot(labels[0], data, linestyle = self.linestyle)
        plt.subplots_adjust(left=None, bottom=None, right=0.75, top=None, wspace=None, hspace=None)
        # if title:
        #     plt.title(title)
        # if x_label:
        #     plt.xlabel(x_label)
        # if y_label:
        #     plt.ylabel(y_label)
        if self.legend:
            if type(labels[1]) == str:
                plt.legend([labels[1]], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
            else:
                plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[0], rotation=90)
        plt.show()

    

def line_plot(data, labels, x_label = None, y_label = None, title = None, legend=False, linestyle = 'solid'):
    plt.plot(labels[0], data, linestyle = linestyle)
    plt.subplots_adjust(left=None, bottom=None, right=0.75, top=None, wspace=None, hspace=None)
    if title:
        plt.title(title)
    if x_label:
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)
    if legend:
        plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
    plt.xticks(labels[0], rotation=90)
    plt.show()

def pie_plot(data, labels):
    plt.pie(data, labels = labels)
    plt.show()

def bar_plot(data, labels):
    if (data.shape[1]> 1):
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        plt.subplots_adjust(left=0.05, bottom=0.25, right=0.85, top=None, wspace=0.5, hspace=None)
        plt.bar(labels[0], data[:, 0], width = 0.6, label=labels[1][0])
        for i, column_label in enumerate(labels[1][1:]):
            plt.bar(labels[0], data[:, i+1],width = 0.6, bottom=np.sum(data[:, :i+1], axis = 1), label=column_label)
        plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[0], rotation=90)

        plt.subplot(1, 2, 2)
        plt.subplots_adjust(left=0.05, bottom=0.25, right=0.85, top=None, wspace=0.5, hspace=None)
        plt.bar(labels[1], data[0, :], width = 0.6, label=labels[0][0])
        for i, column_label in enumerate(labels[0][1:]):
            plt.bar(labels[1], data[i+1, :],width = 0.6, bottom=np.sum(data[:i+1, :], axis = 0), label=column_label)
        plt.legend(labels[0], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[1], rotation=90)
        plt.show()
        
    else:
        plt.bar(labels[0], height = data, tick_label = labels[0])
        plt.xticks(rotation=90)
        plt.show()
    

def box_plot(data, labels):
    plt.boxplot(data, labels = labels)
    plt.xticks(rotation=90)
    plt.show()

def hist_plot(data, bins = None, labels = None):
    plt.hist(data, bins = 10, label = labels)
    plt.subplots_adjust(right=0.75)
    plt.legend(labels, loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
    plt.show()

def plot_all(data, labels):
    if (data.shape[1]> 1):
        plt.figure(figsize=(14, 21))
        plt.subplot(3, 2, 1)
        plt.subplots_adjust(left=0.05, bottom=0.05, right=0.85, top=None, wspace=0.5, hspace=0.5)
        plt.bar(labels[0], data[:, 0], width = 0.6, label=labels[1][0])
        for i, column_label in enumerate(labels[1][1:]):
            plt.bar(labels[0], data[:, i+1],width = 0.6, bottom=np.sum(data[:, :i+1], axis = 1), label=column_label)
        plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[0], rotation=90)

        plt.subplot(3, 2, 2)
        plt.bar(labels[1], data[0, :], width = 0.6, label=labels[0][0])
        for i, column_label in enumerate(labels[0][1:]):
            plt.bar(labels[1], data[i+1, :],width = 0.6, bottom=np.sum(data[:i+1, :], axis = 0), label=column_label)
        plt.legend(labels[0], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[1], rotation=90)

        plt.subplot(3, 2, 3)
        plt.boxplot(data, labels = labels[1])
        plt.xticks(rotation=90)

        plt.subplot(3, 2, 4)
        plt.hist(data, bins = 10, label = labels[1])
        plt.subplots_adjust(right=0.75)
        plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))

        plt.subplot(3, 2, 5)
        plt.pie(np.sum(data, axis = 0), labels = labels[1])

        plt.subplot(3, 2, 6)
        plt.pie(np.sum(data, axis = 1), labels = labels[0])
        plt.show()
        
    else:
        plt.bar(labels[0], height = data, tick_label = labels[0])
        plt.xticks(rotation=90)
        plt.show()


def plot_csv(filename, x_column = None, y_column = 1, row_label = None, column_label = None, title = None, legend=False, linestyle = 'solid', other_graphs = False):
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
        columns_label = list(range(rows.shape[0]))
        data = rows[:, 0:]
    else:
        columns_label = rows[:, 0]
        data = rows[:, 1:]

    labels = (columns_label, fields[1:])

    line_plot(data, labels= labels, x_label = row_label, title = title, legend = legend, linestyle = linestyle)

    if 'all' in other_graphs:
        plot_all(data, labels)

    else:

        if 'hist' in other_graphs:
            hist_plot(data, labels = fields[1:])

        if 'box' in other_graphs:
            box_plot(data, labels = fields[1:])

        if 'pie' in other_graphs:
            pie_plot(np.sum(data, axis = 1), labels = rows[:, 0])
            pie_plot(np.sum(data, axis = 0), labels = fields[1:])

        if 'bar' in other_graphs:
            bar_plot(data, labels = labels)