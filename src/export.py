
from modules import *

class Connect(object):
    def __init__(self, file_name):
        self.cursor = common.Mutual_description(common.Validator(file_name))
        self.make_plots()        
        
    def common_connector(self):
        return {'tables': [self.cursor.show_table()],
                'info': [self.cursor.data_info()],
                'description': [self.cursor.data_description()],
                'shape': [self.cursor.data_shape()]
            }
            

    def plot_list(self):
        return ['/plot{}.png'.format(plot) for plot in range(0, self.cursor.dataset.shape[1])]

    def make_plots(self):
        pass
        # self .cursor.correlations_heatmap()
        # for plot_number in range(self.cursor.dataset.shape[1]):
            # self.cursor.histogram(plot_number)         
        
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
        