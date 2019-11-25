import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from statsmodels import robust

from . import common

class Singular_description(common.Mutual_description):

    def histogram(self):
        sns.distplot(self.dataset['MSSubClass'], rug=True)
        plt.show()

    def measurement(self):
        
        self.dataset.fillna(method='ffill', inplace=True)

        if self.dataset['MasVnrArea'].dtypes == 'float64':    
            for value in self.dataset['MasVnrArea'].values:
                if float(value) != int(value):        
                    return 'quantitive continous'
                    
        if len(pd.unique(self.dataset['MasVnrArea'])) == 2:        
            print(len(pd.unique(self.dataset['MasVnrArea'])))
            return 'quantitive discrete categorical'

        else:
            print(len(pd.unique(self.dataset['MasVnrArea'])))
            return 'quantitive discrete numerical'

    def average(self):
        return np.average(self.dataset['MSSubClass'])

    def expected_value(self):
        return np.mean(self.dataset['MSSubClass'])

    def median(self):
        return np.median(self.dataset['MSSubClass'])

    def mode(self):
        return scipy.stats.mode(self.dataset['MSSubClass'])

    def standard_deviation(self):
        return np.std(self.dataset['MSSubClass'])

    def absolute_deviation_from_mean(self):
        return robust.mad(self.dataset['MSSubClass'])

    def absolute_deviation_from_median(self):
        return scipy.stats.median_absolute_deviation(self.dataset['MSSubClass'])

    def quarter_deviation(self):
        q75, q25 = np.percentile(self.dataset['MSSubClass'], [75 ,25])
        return (q75 - q25)

    def coefficient_of_variation(self):
        return scipy.stats.variation(self.dataset['MSSubClass'])

    def gini_coefficient(self):
        # solve future warning
        mad = np.abs(np.subtract.outer(self.dataset['MSSubClass'], self.dataset['MSSubClass'])).mean()
        rmad = mad/np.mean(self.dataset['MSSubClass'])
        return 0.5 * rmad

    def asymmetry_factor(self):
        return scipy.stats.skew(self.dataset['MSSubClass'])

    def entropy(self):
        return scipy.stats.entropy(self.dataset['MSSubClass'])    
