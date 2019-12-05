
__author__ = 'WJ Maj'

import numpy as np
from scipy import stats

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import SelectKBest, chi2


class Singular_to_all_description(object):
    '''
    Show column relation statistics according to rest columns in data frame.

    Base class for Mutual description instance.

    Outcomes are represented after hoover at the bottom of each
    generated histogram from single.py
    '''
    def anova(self):
        # call for Analysis of Variance from one-vs-all features.
        # send max and min features with score
        # TODO: Refactorize function
        
        max_F_value = -99999999999999999999
        min_F_value = 99999999999999999999
        max_col = ""
        min_col = ""
        
        for column in self.dataset.drop(self.column, axis=1).columns:
            anova_oneway = stats.f_oneway(self.dataset[self.column], self.dataset[column])
            if anova_oneway[0] > max_F_value:
                max_col = column
                max_F_value = anova_oneway[0]
            if anova_oneway[0] <= min_F_value:
                min_col = column
                min_F_value = anova_oneway[0]
            else:
                pass
                
        return [max_col, max_F_value, min_col, min_F_value]

    def discriminant_analysis(self):
        # call for LDA score from one-vs-all features.
        # TODO: Refactorize function

        for column in self.dataset.columns:
            self.dataset[column] = self.dataset[column].astype('int64')

        try:
            clf = LinearDiscriminantAnalysis().fit(self.dataset.drop(self.column, axis=1), self.dataset[self.column])
            return clf.score(self.dataset.drop(self.column, axis=1), self.dataset[self.column])
        except ValueError:
            return 'Inappropiate data'
        
        
    def relevance(self):
        # call for two most relevant features with this feature.
        # TODO: Refactorize function

        bestfeatures = SelectKBest(score_func=chi2).fit(self.dataset.drop(self.column, axis=1), self.dataset[self.column])
        select_best = list(np.array(bestfeatures.scores_))
        
        select_k_best = []
        for k in range(2):
            select_k_best.append(self.dataset.columns[select_best.index(max(select_best))])
            select_best.pop(select_best.index(max(select_best)))
        return select_k_best

