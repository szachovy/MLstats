
from modules import *

class Connect(object):
    def __init__(self, file_name):
        self.cursor = common.Mutual_description(common.Validator(file_name))
        self.data = {}
        
    def common_connector(self):
        self.data['tables'] = [self.cursor.show_table()]
        self.data['info'] = [self.cursor.data_info()]
        self.data['description'] = [self.cursor.data_description()]        
        self.data['corr_heatmap'] = self.cursor.correlations_heatmap()        
    def single_connector(self):
        # single.Single_description.column = 'MSSubClass'
        self.cursor.column = 'MSSubClass'
        print(self.cursor.average())

    def mixed_connector(self):
        print(self.cursor.anova())
        