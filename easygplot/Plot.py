import matplotlib.pyplot as plt
import csv
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class Line(object):
    """
    This module helps in plotting Line Graph on a csv file read by 'easygplot.read(...filename...)'
    Parameters
    ----------
    sample : 'easygplot.read.CSV(...filename...)' object, optional (if the object will be passed while calling the object this class)
        Pass the data and labels read by the 'easygplot.read(...filename...)'.
    figsize : tuple, optional (default = (8, 5))
        first and second element in tuple represent the dimensions of the line graph, which are 
        width and height respectivily.
    linestyle : str (default = 'solid')
        Set the linestyle of the line
        '-' or 'solid'     =>   solid line
        '--' or 'dashed'   =>   dashed line
        '-.' or 'dashdot'  =>	dash-dotted line
        ':' or 'dotted'    =>	dotted line
        'None' or ' ' or ''=>	draw nothing
    legned : bool (default = False)
        Set to 'True' to place a legend on the Axes.
    do_subplot : Set to 'True', while plotting it as subplot.
    subplot_num : Subplot position number.
    title : str, optional
        The title text of the graph.
    x_label : str, optional
        The label text at x-axis.
    y_label : str, optional
        The label text at x-axis.
    Returns : 
    -------
    sample : 'easygplot.read(...filename...)' object
        It is returned for the purpose of creating a pipeline.

    TODO:
        1. Add support for data without labels.
        2. y-ticks support
        3. Smart way to handle data flow through pipeline.
    """
    def __init__ (self, sample = None, figsize = (8, 5), linestyle = 'solid', legend = False, do_subplot = False, subplot_num = None,
    title = None, x_label = None, y_label = None):
        self.sample = sample
        self.figsize = figsize
        self.linestyle = linestyle
        self.legend = legend
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def __call__ (self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(4, 2, self.subplot_num + 1)
        plt.plot(labels[0], data, linestyle = self.linestyle)
        plt.subplots_adjust(left=None, bottom=None, right=0.75, top=None, wspace=None, hspace=None)
        if self.title:
            plt.title(self.title)
        if self.x_label:
            plt.xlabel(self.x_label)
        if self.y_label:
            plt.ylabel(self.y_label)
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
    """
    This module helps in plotting Bar Graph on a csv file read by 'easygplot.read(...filename...)'.
    It plots 2 graphs : one along columns and the other along the rows.
    Parameters
    ----------
    sample : 'easygplot.read.CSV(...filename...)' object, optional (if the object will be passed while calling the object this class)
        Pass the data and labels read by the 'easygplot.read(...filename...)'.
    figsize : tuple, optional (default = (8, 5))
        first and second element in tuple represent the dimensions of the line graph, which are 
        width and height respectivily.
    legned : bool (default = False)
        Set to 'True' to place a legend on the Axes.
    do_subplot : Set to 'True', while plotting it as subplot.
    subplot_num : Subplot position number.
    title : str, optional
        The title text of the graph.
    y_label : str, optional
        The label text at x-axis.
    Returns : 
    -------
    sample : 'easygplot.read(...filename...)' object
        It is returned for the purpose of creating a pipeline.
    """
    def __init__ (self, sample = None, figsize = (8, 5), legend = False, do_subplot = False, subplot_num = None,
    title = None, y_label = None):
        self.sample = sample
        self.figsize = figsize
        self.legend = legend
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num
        self.title = title
        self.y_label = y_label

    def __call__(self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(4, 2, self.subplot_num + 1)
        if len(data.shape) == 1:
            plt.bar(labels[0], data, width = 0.6, label=labels[1][0])
        else:
            plt.bar(labels[0], data[:, 0], width = 0.6, label=labels[1][0])
            if self.title:
                plt.title(self.title)
            if self.y_label:
                plt.ylabel(self.y_label)
            for i, column_label in enumerate(labels[1][1:]):
                plt.bar(labels[0], data[:, i+1],width = 0.6, bottom=np.sum(data[:, :i+1], axis = 1), label=column_label)
        if self.legend:
            if type(labels[1]) == str:
                plt.legend([labels[1]], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
            else:
                plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        plt.xticks(labels[0], rotation=90)
        if not self.do_subplot:
            plt.show()

        if len(data.shape) != 1:
            if not self.do_subplot:
                plt.figure(figsize=self.figsize)
            if self.do_subplot:
                plt.subplot(4, 2, self.subplot_num + 2)
            plt.bar(labels[1], data[0, :], width = 0.6, label=labels[0][0])
            if self.title:
                plt.title(self.title)
            if self.y_label:
                plt.ylabel(self.y_label)
            for i, column_label in enumerate(labels[0][1:]):
                plt.bar(labels[1], data[i+1, :],width = 0.6, bottom=np.sum(data[:i+1, :], axis = 0), label=column_label)
            if self.legend:
                plt.legend(labels[0], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
            plt.xticks(labels[1], rotation=90)
            if not self.do_subplot:
                plt.show()
                return self.sample

class Box(object):
    """
    This module helps in plotting Box Graph on a csv file read by 'easygplot.read(...filename...)'
    Parameters
    ----------
    sample : 'easygplot.read.CSV(...filename...)' object, optional (if the object will be passed while calling the object this class)
        Pass the data and labels read by the 'easygplot.read(...filename...)'.
    figsize : tuple, optional (default = (8, 5))
        first and second element in tuple represent the dimensions of the line graph, which are 
        width and height respectivily.
    legned : bool (default = False)
        Set to 'True' to place a legend on the Axes.
    do_subplot : Set to 'True', while plotting it as subplot.
    subplot_num : Subplot position number.
    title : str, optional
        The title text of the graph.
    x_label : str, optional
        The label text at x-axis.
    y_label : str, optional
        The label text at x-axis.
    Returns : 
    -------
    sample : 'easygplot.read(...filename...)' object
        It is returned for the purpose of creating a pipeline.
    """
    def __init__ (self, sample = None, figsize = (8, 5), do_subplot = False, subplot_num = None,
    title = None, x_label = None, y_label = None):
        self.sample = sample
        self.figsize = figsize
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def __call__(self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(4, 2, self.subplot_num + 1)
        plt.boxplot(data, labels = labels[1])
        if self.title:
            plt.title(self.title)
        if self.x_label:
            plt.xlabel(self.x_label)
        if self.y_label:
            plt.ylabel(self.y_label)
        plt.xticks(rotation=90)
        if not self.do_subplot:
            plt.show()
            return self.sample

class Histogram(object):
    """
    This module helps in plotting Histogram on a csv file read by 'easygplot.read(...filename...)'
    Parameters
    ----------
    sample : 'easygplot.read.CSV(...filename...)' object, optional (if the object will be passed while calling the object this class)
        Pass the data and labels read by the 'easygplot.read(...filename...)'.
    figsize : tuple, optional (default = (8, 5))
        first and second element in tuple represent the dimensions of the line graph, which are 
        width and height respectivily.
    legned : bool (default = False)
        Set to 'True' to place a legend on the Axes.
    do_subplot : Set to 'True', while plotting it as subplot.
    subplot_num : Subplot position number.
    title : str, optional
        The title text of the graph.
    x_label : str, optional
        The label text at x-axis.
    y_label : str, optional
        The label text at x-axis.
    Returns : 
    -------
    sample : 'easygplot.read(...filename...)' object
        It is returned for the purpose of creating a pipeline.
    """
    def __init__ (self, sample = None, figsize = (8, 5), legend = False, do_subplot = False, subplot_num = None,
    title = None, x_label = None, y_label = None):
        self.sample = sample
        self.figsize = figsize
        self.legend = legend
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def __call__(self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(4, 2, self.subplot_num + 1)
        plt.hist(data, bins = 10, label = labels[1])
        plt.subplots_adjust(right=0.75)
        if self.title:
            plt.title(self.title)
        if self.x_label:
            plt.xlabel(self.x_label)
        if self.y_label:
            plt.ylabel(self.y_label)
        if self.legend:
            if type(labels[1]) == str:
                plt.legend([labels[1]], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
            else:
                plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.4, 0, 1, 1))
        if not self.do_subplot:
            plt.show()
            return self.sample

class Pie(object):
    """
    This module helps in plotting Pie Graph on a csv file read by 'easygplot.read(...filename...)'
    It plots 2 graphs : one along columns and the other along the rows.
    Parameters
    ----------
    sample : 'easygplot.read.CSV(...filename...)' object, optional (if the object will be passed while calling the object this class)
        Pass the data and labels read by the 'easygplot.read(...filename...)'.
    figsize : tuple, optional (default = (8, 5))
        first and second element in tuple represent the dimensions of the line graph, which are 
        width and height respectivily.
    legned : bool (default = False)
        Set to 'True' to place a legend on the Axes.
    do_subplot : Set to 'True', while plotting it as subplot.
    subplot_num : Subplot position number.
    title : str, optional
        The title text of the graph.
    x_label : str, optional
        The label text at x-axis.
    y_label : str, optional
        The label text at x-axis.
    Returns : 
    -------
    sample : 'easygplot.read(...filename...)' object
        It is returned for the purpose of creating a pipeline.
    """
    def __init__ (self, sample = None, figsize = (8, 5), legend = False, do_subplot = False, subplot_num = None,
    title_cwise = None, title_rwise = None):
        self.sample = sample
        self.figsize = figsize
        self.legend = legend
        self.do_subplot = do_subplot
        self.subplot_num = subplot_num
        self.title_cwise = title_cwise
        self.title_rwise = title_rwise

    def __call__(self, sample = None):
        if sample:
            self.sample = sample
        data, labels = self.sample
        if not self.do_subplot:
            plt.figure(figsize=self.figsize)
        if self.do_subplot:
            plt.subplot(4, 2, self.subplot_num + 1)
        if len(data.shape) == 1:
            plt.pie(data, labels = labels[0])
        else:
            plt.pie(np.sum(data, axis = 0), labels = labels[1])
            if self.title_cwise:
                plt.title(self.title_cwise)
        if self.legend:
            if type(labels[1]) == str:
                plt.legend([labels[1]], loc='upper right', bbox_to_anchor=(0.6, 0, 1, 1))
            else:
                plt.legend(labels[1], loc='upper right', bbox_to_anchor=(0.6, 0, 1, 1))
        if not self.do_subplot:
            plt.show()

        if len(data.shape) != 1:
            if not self.do_subplot:
                plt.figure(figsize=self.figsize)
            if self.do_subplot:
                plt.subplot(4, 2, self.subplot_num + 2)
            plt.pie(np.sum(data, axis = 1), labels = labels[0])
            if self.title_rwise:
                plt.title(self.title_rwise)
            if self.legend:
                plt.legend(labels[0], loc='upper right', bbox_to_anchor=(0.6, 0, 1, 1))
            if not self.do_subplot:
                plt.show()
                return self.sample

class Subplots:
    """
    Plot the different graphs using 'easygplot.read.CSV(...filename...)' object.
    Parameters
    ----------
    sample : 'easygplot.read.CSV(...filename...)' object
        Pass the data and labels read by the 'easygplot.read(...filename...)'.
    Output
    ------
    Subplots of all the input graph types
    """
    def __init__(self, sample, legend = False):
        self.sample = sample
        self.legend = legend

    def __call__(self, *args):
        """
        *args : array-like strings
            Input the graphs names which you to display
            'all' => plot all graphs
            Individual graphs are: {'line', 'box', 'pie', 'bar', 'histogram'}
        """
        all_plots = []
        num_subplots = 0

        if 'all' in args:
            if len(self.sample[0].shape) == 1:
                subplot_num = (1, 2, 3)
                num_subplots = 5
            else:
                subplot_num = (2, 4, 6)
                num_subplots = 7
            all_plots += [Line(sample = self.sample, legend = True, do_subplot= True, subplot_num = 0)]
            if len(self.sample[0].shape) != 1:
                all_plots += [Box(sample = self.sample, do_subplot= True, subplot_num = 1)]
            all_plots += [Pie( sample = self.sample, legend = True, do_subplot= True, subplot_num = subplot_num[0])]
            all_plots += [Bar( sample = self.sample, legend = True, do_subplot= True, subplot_num = subplot_num[1])]
            all_plots += [Histogram( sample = self.sample, legend = True, do_subplot= True, subplot_num = subplot_num[2])]
                

        else:
            if 'line' in args:
                all_plots += [Line(sample = self.sample, legend = True, do_subplot= True, subplot_num = num_subplots)]
                num_subplots += 1
            if 'box' in args:
                all_plots += [Box(sample = self.sample, do_subplot= True, subplot_num = num_subplots)]
                num_subplots += 1
            if 'pie' in args:
                all_plots += [Pie(sample = self.sample, legend = True, do_subplot= True, subplot_num = num_subplots)]
                num_subplots += 2
            if 'bar' in args:
                all_plots += [Bar(sample = self.sample, legend = True, do_subplot= True, subplot_num = num_subplots)]
                if len(self.sample) == 1:
                    num_subplots += 1
                else:
                    num_subplots += 2
            if 'histogram' in args:
                all_plots += [Histogram(sample = self.sample, legend = True, do_subplot= True, subplot_num = num_subplots)]
                num_subplots += 1

        # subplot_ratio = int(num_subplots/2 + 1)
        plt.figure(figsize=(16, 24))
        for plot in all_plots:
            plt.subplots_adjust(left=0.05, bottom=0.05, right=0.85, top=None, wspace=0.5, hspace=0.5)
            plot()