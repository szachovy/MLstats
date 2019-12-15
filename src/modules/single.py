

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from statsmodels import robust

class Singular_description(object):
    '''
    Display statistics from every numerical column in data set.

    Base class for Mutual description instance.

    Outcomes are represented from the beggining (after hoover),
    in each histogram plot in the page.

    Class covers the most general feature statistics used in data analysis.
    '''
    
    def __init__(self):
        # Handled by cursor in common.py file in `Mutual_description`
        self.column = ""


    def histogram(self, plot_number):
        # Generate histogram and save as a static file
        # size and ticks are adjusted with accordance to display size
        sns.set_style("whitegrid")
        
        fig, ax = plt.subplots()
        fig.set_size_inches(12, 12)
        
        ax=sns.distplot(self.dataset.iloc[:, [plot_number]], rug=True, color='k')
        fig.patch.set_alpha(0.0)
        
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        
        fig.savefig('static/plot{}.png'.format(plot_number + 1), dpi=fig.dpi)
        # return fig
        # plt.show()

    def measurement(self):
        # call for measurement category of the feature
        # possible outcomes are:
        # -- quantitive continous
        # -- quantitive discrete categorical
        # -- quantitive discrete numerical

        if self.dataset[self.column].dtypes == 'float64':    
            for value in self.dataset[self.column].values:
                if float(value) != int(value):        
                    return 'quantitive continous'
                    
        if len(pd.unique(self.dataset[self.column])) == 2:        
            return 'quantitive discrete categorical'

        else:
            return 'quantitive discrete numerical'


    def average(self):
        # TODO: remove        
        return np.average(self.dataset[self.column])

    def expected_value(self):
        # call for expected value from feature distribution 
        return np.mean(self.dataset[self.column])

    def median(self):
        # call for median from feature distribution
        return np.median(self.dataset[self.column])

    def mode(self):
        # call for mode from feature distribution
        return scipy.stats.mode(self.dataset[self.column])

    def standard_deviation(self):
        # call for standard deviation from feature distribution
        return np.std(self.dataset[self.column])

    def absolute_deviation_from_mean(self):
        # call for absolute deviation from mean from feature distribution
        return np.mean(np.absolute(self.dataset[self.column] - np.mean(self.dataset[self.column])))

    def absolute_deviation_from_median(self):
        # call for mode from feature distribution
        return scipy.stats.median_absolute_deviation(self.dataset[self.column])

    def quarter_deviation(self):
        # call for quarter devaition from feature distribution
        q75, q25 = np.percentile(self.dataset[self.column], [75 ,25])
        return (q75 - q25)

    def coefficient_of_variation(self):
        # call for coefficient of variation from feature distribution  
        return scipy.stats.variation(self.dataset[self.column])

    def gini_coefficient(self):
        # call for gini coefficient from feature distribution
        # TODO: refactorize 
        mad = np.abs(np.subtract.outer(self.dataset[self.column], self.dataset[self.column])).mean()
        rmad = mad/np.mean(self.dataset[self.column])
        return 0.5 * rmad

    def asymmetry_factor(self):
        # call for asymmetry factor from feature distribution
        return scipy.stats.skew(self.dataset[self.column])

    def entropy(self):
        # call for entropy from feature distribution   
        return scipy.stats.entropy(self.dataset[self.column])    
