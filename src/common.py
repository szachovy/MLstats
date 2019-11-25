import numpy as np
import pandas as pd
from itertools import compress
import matplotlib.pyplot as plt
import seaborn as sns

class Extract(object):
    def __init__(self, file_name):
        self.dataset = self.check_input(file_name)

    @staticmethod
    def check_input(file_name):
        if file_name.endswith('.csv'):
            dataset = pd.read_csv(file_name)
                
        elif file_name.endswith('.xlsx'):
            dataset = pd.read_excel(file_name)
                            
        elif file_name.endswith('.json'):
            dataset = pd.read_json(file_name)    
            
        else:
            raise Exception('selected input file data format is not supported')   

        index_column = list(compress(dataset.columns, ['Unnamed' in dataset.columns[index] for index in range(dataset.shape[1])]))
        if index_column:
            for index in [dataset.columns.get_loc(index) for index in index_column]:
                if ((np.array_equal(dataset[dataset.columns[index]], [value+1 for value in range(len(dataset[dataset.columns[index]]))])) or (np.array_equal(dataset[dataset.columns[index]], [value+1 for value in range(len(dataset[dataset.columns[index]]))]))):
                    dataset.drop(dataset.columns[index], axis=1, inplace=True)
                
        return dataset

class Mutual_description(object):
    def __init__(self, file_name):
        self.dataset = Extract.check_input(file_name)
        
    def show_table(self):
        return self.dataset.to_html(classes='data', header="true")

    def data_info(self):
        return self.dataset.info()

    def data_description(self):
        return self.dataset.describe()

    def correlations_heatmap(self):
        # save plot then send a picture to flask
        fig, ax = plt.subplots()
        fig.set_size_inches(24, 16)
        
        ax=sns.heatmap(self.dataset.corr(), annot=True, linewidths=.5, cmap="YlGnBu", fmt='.1f')
        plt.show()
