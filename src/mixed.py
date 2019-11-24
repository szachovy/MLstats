import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import SelectKBest, chi2

from . import common

class Singular_to_all_description(common.Mutual_description):

    def anova(self):
        self.dataset = self.dataset.select_dtypes(exclude=['object'])
        self.dataset.dropna(inplace=True)
        # for loop for every
        return stats.f_oneway(self.dataset['MSSubClass'], self.dataset['LotFrontage'])


    def discriminant_analysis(self):
        clf = LinearDiscriminantAnalysis().fit(self.dataset, self.dataset['MSSubClass'] )
        return clf.score(self.dataset, self.dataset['MSSubClass'])
        
    def relevance(self):
        bestfeatures = SelectKBest(score_func=chi2, k=10).fit(self.dataset, self.dataset['MSSubClass'] )
        return np.array(bestfeatures.scores_)

