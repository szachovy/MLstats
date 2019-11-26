import pandas as pd
from flask import Flask, Response, request, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import io

from src import export

# class Routing(object):
    # app = Flask(__name__)
    # file_name = ""
    # connection = ""
    # plot_number = 0
    # 
    # @app.route('/')
    # def upload():
        # return render_template("upload.html")
# 
  
    # @app.route('/plot0.png')
    # def plot_png():
        # fig = []
        # if not Response.plot_number:
            # fig = Routing.connection.heatmap()
        # else:
            # fig = Routing.connection.histplot(Response.plot_number - 1)
# 
        # Response.plot_number += 1
        # output = io.BytesIO()
        # FigureCanvas(fig).print_png(output)
        # return Response(output.getvalue(), mimetype='image/png')
# 
# 
    # @app.route('/describe', methods = ['POST'])
    # def success():
        # if request.method == 'POST':
            # Routing.file_name = request.files['file'].filename
            # Routing.connection = export.Connect(Routing.file_name)
            # 
                # return render_template("describe.html", tables = Routing.connection.data['tables'],
                    # info = Routing.connection.data['info'],
                    # description =  Routing.connection.data['description'],
                # )
                                
            # return render_template("describe.html", common = Routing.connection.common_connector(),
                        # single = Routing.connection.single_connector(),
                        # mixed = Routing.connection.mixed_connector())
                # 
            # except Exception:
                # return render_template("upload.html") #, error = 'Incorrect data format'
        # else:
            # return render_template("upload.html") #, error = 'File not provided'

    
# 
      # 
# if __name__ == '__main__':
    # Routing.app.run(debug = True)

if __name__ == '__main__':
    connection = export.Connect('train.csv')
    single = connection.single_connector()
    # print(single.keys())
    mixed = connection.mixed_connector()
    print(mixed['MSSubClass'])
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
