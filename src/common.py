import numpy as np
import pandas as pd
from itertools import compress

class Extract(object):
    def __init__(self, dataset):
        self.dataset = self.unpack(dataset)

    @classmethod
    def check_input(cls, file_name):
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
                
        return cls(dataset)