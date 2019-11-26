import numpy as np
from scipy import stats
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import SelectKBest, chi2


class Singular_to_all_description(object):

    def anova(self):
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
                
        return [max_col, min_col]

    def discriminant_analysis(self):
        for column in self.dataset.columns:
            self.dataset[column] = self.dataset[column].astype('int64')
        # clf = LinearDiscriminantAnalysis().fit(self.dataset, self.dataset[self.column])
        # return clf.score(self.dataset, self.dataset[self.column])
        return True
        
    def relevance(self):
        # select two most relevant

        bestfeatures = SelectKBest(score_func=chi2).fit(self.dataset.drop(self.column, axis=1), self.dataset[self.column])
        select_best = list(np.array(bestfeatures.scores_))
        
        select_k_best = []
        for k in range(2):
            select_k_best.append(self.dataset.columns[select_best.index(max(select_best))])
            select_best.pop(select_best.index(max(select_best)))
        return select_k_best

