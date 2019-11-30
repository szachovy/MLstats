import pandas as pd
from flask import Flask, Response, request, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import io

from src import export

# class App(Flask):
    # def __init__():
        # Flask.__init__()
        # self.plot_number = 0

# def create_app(dzialaj):
    # app = Flask(__name__)
    # app.config['plot_number'] = dzialaj
# 
    # return app

app = Flask(__name__) 
app.config['plot_number'] = 0

class Routing(object):
    # app = create_app(dzialaj)
    # app.config['plot_number'] = 0
    file_name = ""
    connection = ""
    
    @app.route('/')
    def upload():
        return render_template("upload.html")
# 
  
    # @app.route('/plot<plot_number>.png')
    # def plot_png(plot_number = app.config['plot_number']):

        # if not app.config['plot_number']:
            # fig = Routing.connection.heatmap()
        # else:
            # fig = Routing.connection.histplot(app.config['plot_number'] - 1)

        # app.config['plot_number'] += 1
        # output = io.BytesIO()
        # FigureCanvas(fig).print_png(output)
        # return Response(output.getvalue(), mimetype='image/png')
# 
# 
    @app.route('/describe', methods = ['POST'])
    def success():
        if request.method == 'POST':
            Routing.file_name = request.files['file'].filename
            Routing.connection = export.Connect(Routing.file_name)

            return render_template("describe.html", common = Routing.connection.common_connector(),
                        single = Routing.connection.single_connector(),
                        mixed = Routing.connection.mixed_connector(),
                        plots = Routing.connection.plot_list() 
                        )
    
        else:
            return render_template("upload.html") #, error = 'File not provided'

    

      
if __name__ == '__main__':
    app.run(debug = True)

# if __name__ == '__main__':
    # connection = export.Connect('train.csv')
    # connection.histplot(1)

    # mixed = connection.mixed_connector()
    # print(mixed)
    # data = export.Connect('train.csv')
    # data.common_connector()
    # print(data.data)
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
