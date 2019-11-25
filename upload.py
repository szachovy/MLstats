from flask import *  
import pandas as pd
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

from src import common
from src import individual
from src import mixed

class Routing(object):
    app = Flask(__name__)
    file_name = ""
        
    @app.route('/')
    def upload():
        return render_template("upload.html")


    @app.route('/plot.png')
    def plot_png():
        fig = common.Mutual_description(Routing.file_name).correlations_heatmap()
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')


    @app.route('/describe', methods = ['POST'])
    def success():
        if request.method == 'POST':
            Routing.file_name = request.files['file'].filename
            
            mutual = common.Mutual_description(Routing.file_name)
            singular = individual.Singular_description(Routing.file_name)

            return render_template("describe.html", tables = [mutual.show_table()],
                info = [mutual.data_info()],
                description =  [mutual.data_description()],
            ) # singular.average()
    
# 
      
if __name__ == '__main__':
    Routing.app.run(debug = True)

# if __name__ == '__main__':
    # mutual = common.Mutual_description('train.csv')
    # print(mutual.show_table())
    # print(mutual.data_info())
    # print(mutual.data_description())
    # mutual.correlations_heatmap()
    # singular = individual.Singular_description('train.csv')
    # 
    # print(singular.measurement())
    # singular.histogram()
    # print(singular.average())
    # print(singular.expected_value())
    # print(singular.median())
    # print(singular.mode())
    # print(singular.standard_deviation())
    # print(singular.absolute_deviation_from_mean())
    # print(singular.absolute_deviation_from_median())
    # print(singular.quarter_deviation())
    # print(singular.coefficient_of_variation())
    # print(singular.gini_coefficient())
    # print(singular.asymmetry_factor())
    # print(singular.entropy())
 # 
    # compare = mixed.Singular_to_all_description('train.csv')
    # print(compare.anova())
    # print(compare.discriminant_analysis())
    # print(compare.relevance())
