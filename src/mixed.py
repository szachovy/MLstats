import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

from . import common

class Singular_to_all_description(common.Mutual_description):
    def __init__(self, file_name):
        super().__init__(file_name)
        
    def anova(self):
        # return stats.f_oneway(tillamook, newport, petersburg, magadan, tvarminne)
        pass

    def relevance(self):
        pass

    def redundancy(self):
        pass

    def interaction(self):
        pass

