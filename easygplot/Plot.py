import matplotlib.pyplot as plt
import csv
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class Line(object):
    def __init__ (self, figsize = (8, 5), linestyle = 'solid', legend = False, sample = None):
        self.figsize = figsize
        self.linestyle = linestyle
        self.legend = legend
        self.sample = sample

    def __call__ (self, sample):
        self.sample = sample
        data, labels = self.sample
        plt.figure(figsize=self.figsize)
        plt.plot(labels[0], data, linestyle = self.linestyle)
        # plt.subplots_adjust(left=None, bottom=None, right=0.75, top=None, wspace=None, hspace=None)
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
        return self.sample

class Bar(object):
    def __init__ (self, figsize = (8, 5), legend = False, sample = None):
        self.figsize = figsize
        self.legend = legend
        self.sample = sample
    def __call__(self, sample):
        self.sample = sample
        data, labels = self.sample
        plt.figure(figsize=self.figsize)
        plt.bar(labels[0], data[:, 0], width = 0.6, label=labels[1][0])
        for i, column_label in enumerate(labels[1][1:]):
            plt.bar(labels[0], data[:, i+1],width = 0.6, bottom=np.sum(data[:, :i+1], axis = 1), label=column_label)
        if self.legend:
            plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[0], rotation=90)
        plt.show()

        plt.figure(figsize=self.figsize)
        plt.bar(labels[1], data[0, :], width = 0.6, label=labels[0][0])
        for i, column_label in enumerate(labels[0][1:]):
            plt.bar(labels[1], data[i+1, :],width = 0.6, bottom=np.sum(data[:i+1, :], axis = 0), label=column_label)
        if self.legend:
            plt.legend(labels[0], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[1], rotation=90)
        plt.show()
        return self.sample

class Box(object):
    def __init__ (self, figsize = (8, 5), sample = None):
        self.figsize = figsize
        self.sample = sample
    def __call__(self, sample):
        self.sample = sample
        data, labels = self.sample
        plt.figure(figsize=self.figsize)
        plt.boxplot(data, labels = labels[1])
        plt.xticks(rotation=90)
        plt.show()
        return self.sample

class Histogram(object):
    def __init__ (self, figsize = (8, 5), legend = False, sample = None):
        self.figsize = figsize
        self.legend = legend
        self.sample = sample
    def __call__(self, sample):
        self.sample = sample
        data, labels = self.sample
        plt.figure(figsize=self.figsize)
        plt.hist(data, bins = 10, label = labels[1])
        plt.subplots_adjust(right=0.75)
        if self.legend:
            plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.show()
        return self.sample

class Pie(object):
    def __init__ (self, figsize = (8, 5), legend = False, sample = None):
        self.figsize = figsize
        self.legend = legend
        self.sample = sample
    def __call__(self, sample):
        self.sample = sample
        data, labels = self.sample
        plt.figure(figsize=self.figsize)
        plt.pie(np.sum(data, axis = 0), labels = labels[1])
        if self.legend:
            plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.6, 0, 1, 1))
        plt.show()

        plt.figure(figsize=self.figsize)
        plt.pie(np.sum(data, axis = 1), labels = labels[0])
        if self.legend:
            plt.legend(labels[0], loc='upper right', bbox_to_anchor=(0.6, 0, 1, 1))
        plt.show()
        return self.sample

class Subplots:
    def __init__(self, *args, **kwargs):
        pass