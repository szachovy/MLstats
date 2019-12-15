

from flask import Flask
import numpy as np
import pandas as pd
from itertools import compress
import matplotlib.pyplot as plt
import seaborn as sns
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

############### self defined
from . import single
from . import mixed

###########################

class Validator(object):
    '''
    Validate input file name
    Match with indices, export all except 'Unnamed*'
    '''
    def __new__(cls, file_name):
        '''
        Preinitalize with class method

        Returns:
            func: checking input func (change data format)
        '''
        return cls.check_input(file_name)

        
    def check_input(file_name):
        '''
        Checks input file before analysis
        
        Raises:
            Exception: file data is not supported (this couldn`t happened)

        Returns:
            dataset: extracted pandas dataframe

        '''
        if file_name.endswith('.csv'):
            dataset = pd.read_csv(file_name)
                
        elif file_name.endswith('.xlsx'):
            dataset = pd.read_excel(file_name)
                            
        elif file_name.endswith('.json'):
            dataset = pd.read_json(file_name)    
            
        else:
            raise Exception('selected input file data format is not supported')   

        # find unnamed columns
        index_column = list(compress(dataset.columns, ['Unnamed' in dataset.columns[index] for index in range(dataset.shape[1])]))
        
        if index_column:
            for index in [dataset.columns.get_loc(index) for index in index_column]:
                if ((np.array_equal(dataset[dataset.columns[index]], [value+1 for value in range(len(dataset[dataset.columns[index]]))])) or (np.array_equal(dataset[dataset.columns[index]], [value+1 for value in range(len(dataset[dataset.columns[index]]))]))):
                    dataset.drop(dataset.columns[index], axis=1, inplace=True)
                
        return dataset

class Mutual_description(single.Singular_description, mixed.Singular_to_all_description):
    '''
    Show joint dependencies and general description
    accross mutual features in data set.

    Mutual features handle raw data set,
    include all informations directly from file.

    - This class is operating by cursor
    '''
    def __init__(self, dataset):
        '''
        General initializator handled by cursor in connection functions.
        
        Includes base class initializator (cursor send column info by base class,
                                            but mutual initializator is here.)

        Args:
            dataset: validated data frame.
        '''
        self.dataset_uncorrected = dataset
        super().__init__()        
        self.dataset = dataset.select_dtypes(exclude=['object'])
        self.dataset.fillna(method='ffill', inplace=True)

    def show_table(self):
        # call for data table in request from cursor
        return self.dataset_uncorrected.to_html(classes='data', header="true")

    def data_info(self):
        # call for data information in request from cursor
        # information includes:
        # -- Data types
        # -- Null occurrences
        # -- Memory usage
        # (presented in table)        
        
        dict_info = {}
        for column in self.dataset_uncorrected.columns:
            dict_info[column] = [self.dataset_uncorrected.loc[:,column].dtype, self.dataset_uncorrected.loc[:,column].isna().sum(), self.dataset_uncorrected.loc[:,column].memory_usage(deep=True)]

        data_info = pd.DataFrame(data=dict_info).transpose()
        data_info.columns = ['Data Type', 'Null Occurences', 'Memory usage']
        return data_info.to_html(classes='data', header="true")
        

    def data_description(self):
        # call for data description in request from cursor
        # description includes:
        # -- count
        # -- mean
        # -- standard deviation
        # -- min
        # -- first quartile
        # -- median
        # -- third quartuile
        # -- max
        # (presented in table)
        return self.dataset_uncorrected.describe().to_html(classes='data', header="true")

    def data_shape(self):
        # call for data rows and cols as matrix shape
        return self.dataset_uncorrected.shape
        
    def correlations_heatmap(self):
        # call for correlation heatmap of all numerical features accross data frame
        # correlation range is adapted on the right bar
        # plot size and ticks are adjusted according to display size
        
        sns.set()
        fig, ax = plt.subplots()
        fig.set_size_inches(28, 21)
        
        ax=sns.heatmap(self.dataset_uncorrected.corr(), annot=True, linewidths=1, cmap="Greys", fmt='.2f')

        plt.xticks(fontsize=16, rotation=70)
        plt.yticks(fontsize=16)
        
        fig.patch.set_alpha(0.0)
        fig.savefig('static/plot0.png', dpi=fig.dpi)

        return fig
        # plt.show()
