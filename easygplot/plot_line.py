import matplotlib.pyplot as plt
import csv
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class plot_line(object):
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
        return self.sample
