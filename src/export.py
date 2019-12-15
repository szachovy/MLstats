

from flask import url_for
import os

####### self defined
from modules import *

####################

class Connect(object):
    '''
    Universal connector between upload and python modules
    '''
    def __init__(self, file_name):
        '''
        Transfer file.
        Cursor references to function calls from __all__ files from modules
        
        Args:
            file_name: file name from .. catalog
            
        '''
        self.cursor = common.Mutual_description(common.Validator(file_name))
        self.make_plots()        
        
    def common_connector(self) -> dict:
        '''
        Connect to common file functions in order to get common data set features.

        ** This part is represented as general tables in the front of describe.html **

        Returns:
            dict: results in render_template(`common`)   
                
        '''
        return {'tables': [self.cursor.show_table()],
                'info': [self.cursor.data_info()],
                'description': [self.cursor.data_description()],
                'shape': [self.cursor.data_shape()]
            }
            

    def plot_url_list(self) -> list:
        '''
        List of plots url names generated in /static
        Used as reference from describe.html file.

        Returns:
            list: results in render_template(`plot_url_list`)            
        '''
        return [[plot, url_for('static', filename='plot{}.png'.format(plot))] for plot in range(1, self.cursor.dataset.shape[1])]

    def make_plots(self):
        '''
        Make heatmap and histograms directly from __init__,
        Did the biggest thing firstly.
        
        '''
        self.cursor.correlations_heatmap()
        for plot_number in range(self.cursor.dataset.shape[1]):
            self.cursor.histogram(plot_number)
        
    def single_connector(self) -> dict:
        '''
        General description for every column in data set (which is represented as float64 or int64)
        
        ** This part is represented as values after hoover on histogram (single values) **     

        Returns:
            dict: results in render_template(`single`)
        '''
        single = {}
        
        for column in self.cursor.dataset.columns:
            self.cursor.column = column
            single[self.cursor.dataset.columns.get_loc(column) + 1] = [column, self.cursor.measurement(),
                                self.cursor.average(), self.cursor.expected_value(),
                                self.cursor.median(), self.cursor.mode(), self.cursor.standard_deviation(),
                                self.cursor.absolute_deviation_from_mean(), self.cursor.absolute_deviation_from_median(),
                                self.cursor.quarter_deviation(), self.cursor.coefficient_of_variation(),
                                self.cursor.gini_coefficient(), self.cursor.asymmetry_factor(),
                                self.cursor.entropy()]
            
        return single
            

    def mixed_connector(self) -> dict:
        '''
        This is special use case of function call One-Vs-All column,
        implemented singularly.
        
        ** This part is represented as values after hoover on histogram (single values) **     

        Returns:
            dict: results in render_template(`single`)        
        '''
        mixed = {}
        
        for column in self.cursor.dataset.columns:
            self.cursor.column = column
            mixed[self.cursor.dataset.columns.get_loc(column) + 1] = [self.cursor.anova(), self.cursor.discriminant_analysis(), self.cursor.relevance()]

            
        return mixed
        
