
from modules import *

class Connect(object):
    def __init__(self, file_name):
        self.cursor = common.Mutual_description(common.Validator(file_name))
        
    def common_connector(self):
        return {'tables': [self.cursor.show_table()],
                'info': [self.cursor.data_info()],
                'description': [self.cursor.data_description()]
            }
            
    def heatmap(self):
        return self.cursor.correlations_heatmap()

    def histplot(self, plot_number):
        return self.cursor.histogram(plot_number)
        
    def single_connector(self):
        single = {}
        for column in self.cursor.dataset.columns:
            self.cursor.column = column
            single[column] = [self.cursor.measurement(), self.cursor.average(), self.cursor.expected_value(),
                                self.cursor.median(), self.cursor.mode(), self.cursor.standard_deviation(),
                                self.cursor.absolute_deviation_from_mean(), self.cursor.absolute_deviation_from_median(),
                                self.cursor.quarter_deviation(), self.cursor.coefficient_of_variation(),
                                self.cursor.gini_coefficient(), self.cursor.asymmetry_factor(),
                                self.cursor.entropy()]
        return single
            

    def mixed_connector(self):
        mixed = {}
        for column in self.cursor.dataset.columns:
            self.cursor.column = column
            mixed[column] = [self.cursor.anova(), self.cursor.discriminant_analysis(), self.cursor.relevance()]

        return mixed
        