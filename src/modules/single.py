import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from statsmodels import robust

class Singular_description(object):

    def __init__(self):
        self.column = ""


    def histogram(self, plot_number):
        sns.set()
        fig, ax = plt.subplots()
        fig.set_size_inches(24, 16)
        
        ax=sns.distplot(self.dataset.iloc[:, [plot_number]], rug=True)
        fig.patch.set_alpha(0.0)
        fig.savefig('static/plot{}.png'.format(plot_number + 1), dpi=fig.dpi)
        # return fig
        # plt.show()

    def measurement(self):

        if self.dataset[self.column].dtypes == 'float64':    
            for value in self.dataset[self.column].values:
                if float(value) != int(value):        
                    return 'quantitive continous'
                    
        if len(pd.unique(self.dataset[self.column])) == 2:        
            return 'quantitive discrete categorical'

        else:
            return 'quantitive discrete numerical'


    def average(self):
        return np.average(self.dataset[self.column])

    def expected_value(self):
        return np.mean(self.dataset[self.column])

    def median(self):
        return np.median(self.dataset[self.column])

    def mode(self):
        return scipy.stats.mode(self.dataset[self.column])

    def standard_deviation(self):
        return np.std(self.dataset[self.column])

    def absolute_deviation_from_mean(self):
        return robust.mad(self.dataset[self.column])

    def absolute_deviation_from_median(self):
        return scipy.stats.median_absolute_deviation(self.dataset[self.column])

    def quarter_deviation(self):
        q75, q25 = np.percentile(self.dataset[self.column], [75 ,25])
        return (q75 - q25)

    def coefficient_of_variation(self):
        return scipy.stats.variation(self.dataset[self.column])

    def gini_coefficient(self):
        # solve future warning
        # change np subrtact here
        mad = np.abs(np.subtract.outer(self.dataset[self.column], self.dataset[self.column])).mean()
        rmad = mad/np.mean(self.dataset[self.column])
        return 0.5 * rmad

    def asymmetry_factor(self):
        return scipy.stats.skew(self.dataset[self.column])

    def entropy(self):
        return scipy.stats.entropy(self.dataset[self.column])    
