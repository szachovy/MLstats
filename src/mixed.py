import numpy as np
from scipy import stats
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import SelectKBest, chi2

from . import common

class Singular_to_all_description(common.Mutual_description):

    def anova(self):
        self.dataset = self.dataset.select_dtypes(exclude=['object'])
        self.dataset.dropna(inplace=True)
        return stats.f_oneway(self.dataset['MSSubClass'], self.dataset['LotFrontage'])

    def discriminant_analysis(self):
        for column in self.dataset.columns:
            self.dataset[column] = self.dataset[column].astype('int64')
        clf = LinearDiscriminantAnalysis().fit(self.dataset, self.dataset['MSSubClass'])
        return clf.score(self.dataset, self.dataset['MSSubClass'])
        
    def relevance(self):
        # select two most relevant
        bestfeatures = SelectKBest(score_func=chi2).fit(self.dataset, self.dataset['MSSubClass'] )
        return np.array(bestfeatures.scores_)

