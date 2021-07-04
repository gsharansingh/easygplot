import matplotlib.pyplot as plt
import csv
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class Line(object):
    def __init__ (self, figsize = (8, 5), linestyle = 'solid', legend = False, sample = None, do_subplot = False, subplot_num = None):
        self.figsize = figsize
        self.linestyle = linestyle
        self.legend = legend
        self.sample = sample
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num

    def __call__ (self, sample = None, num_subplots = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(3, 2, self.subplot_num + 1)
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
        if not self.do_subplot:
            plt.show()
            return self.sample

class Bar(object):
    def __init__ (self, figsize = (8, 5), legend = False, sample = None, do_subplot = False, subplot_num = None):
        self.figsize = figsize
        self.legend = legend
        self.sample = sample
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num

    def __call__(self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(3, 2, self.subplot_num + 1)
        plt.bar(labels[0], data[:, 0], width = 0.6, label=labels[1][0])
        for i, column_label in enumerate(labels[1][1:]):
            plt.bar(labels[0], data[:, i+1],width = 0.6, bottom=np.sum(data[:, :i+1], axis = 1), label=column_label)
        if self.legend:
            plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[0], rotation=90)
        if not self.do_subplot:
            plt.show()

        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(3, 2, self.subplot_num + 2)
        plt.bar(labels[1], data[0, :], width = 0.6, label=labels[0][0])
        for i, column_label in enumerate(labels[0][1:]):
            plt.bar(labels[1], data[i+1, :],width = 0.6, bottom=np.sum(data[:i+1, :], axis = 0), label=column_label)
        if self.legend:
            plt.legend(labels[0], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[1], rotation=90)
        if not self.do_subplot:
            plt.show()
            return self.sample

class Box(object):
    def __init__ (self, figsize = (8, 5), sample = None, do_subplot = False, subplot_num = None):
        self.figsize = figsize
        self.sample = sample
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num

    def __call__(self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(3, 2, self.subplot_num + 1)
        plt.boxplot(data, labels = labels[1])
        plt.xticks(rotation=90)
        if not self.do_subplot:
            plt.show()
            return self.sample

class Histogram(object):
    def __init__ (self, figsize = (8, 5), legend = False, sample = None, do_subplot = False, subplot_num = None):
        self.figsize = figsize
        self.legend = legend
        self.sample = sample
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num

    def __call__(self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(3, 2, self.subplot_num + 1)
        plt.hist(data, bins = 10, label = labels[1])
        plt.subplots_adjust(right=0.75)
        if self.legend:
            plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        if not self.do_subplot:
            plt.show()
            return self.sample

class Pie(object):
    def __init__ (self, figsize = (8, 5), legend = False, sample = None, do_subplot = False, subplot_num = None):
        self.figsize = figsize
        self.legend = legend
        self.sample = sample
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num

    def __call__(self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(3, 2, self.subplot_num + 1)
        plt.pie(np.sum(data, axis = 0), labels = labels[1])
        if self.legend:
            plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.6, 0, 1, 1))
        if not self.do_subplot:
            plt.show()

        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(3, 2, self.subplot_num + 2)
        plt.pie(np.sum(data, axis = 1), labels = labels[0])
        if self.legend:
            plt.legend(labels[0], loc='upper right', bbox_to_anchor=(0.6, 0, 1, 1))
        if not self.do_subplot:
            plt.show()
            return self.sample

class Subplots:
    def __init__(self, sample, legend = False):
        self.legend = legend
        self.sample = sample
    def __call__(self, *args):
        all_plots = []
        num_subplots = 0
        if 'line' in args:
            all_plots += [Histogram(legend = True, sample = self.sample, do_subplot= True, subplot_num = num_subplots)]
            num_subplots += 1

        if 'histogram' in args:
            all_plots += [Histogram(legend = True, sample = self.sample, do_subplot= True, subplot_num = num_subplots)]
            num_subplots += 1

        if 'box' in args:
            all_plots += [Box(sample = self.sample, do_subplot= True, subplot_num = num_subplots)]
            num_subplots += 1

        if 'pie' in args:
            all_plots += [Pie(legend = True, sample = self.sample, do_subplot= True, subplot_num = num_subplots)]
            num_subplots += 2

        if 'bar' in args:
            all_plots += [Bar(legend = True, sample = self.sample, subplot_num = num_subplots)]
            num_subplots += 2

        subplot_ratio = int(num_subplots/2 + 0.5)
        plt.figure(figsize=(subplot_ratio*5, subplot_ratio*3))
        from torchvision import transforms
        plot_obj = transforms.Compose(all_plots)
        return plot_obj