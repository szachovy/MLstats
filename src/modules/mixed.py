import numpy as np
from scipy import stats
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import SelectKBest, chi2


class Singular_to_all_description(object):

    def anova(self):
        self.dataset = self.dataset.select_dtypes(exclude=['object'])
        self.dataset.dropna(inplace=True)
        return stats.f_oneway(self.dataset[self.column], self.dataset['LotFrontage'])

    def discriminant_analysis(self):
        for column in self.dataset.columns:
            self.dataset[column] = self.dataset[column].astype('int64')
        clf = LinearDiscriminantAnalysis().fit(self.dataset, self.dataset[self.column])
        return clf.score(self.dataset, self.dataset[self.column])
        
    def relevance(self):
        # select two most relevant
        bestfeatures = SelectKBest(score_func=chi2).fit(self.dataset, self.dataset[self.column])
        return np.array(bestfeatures.scores_)

