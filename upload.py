import pandas as pd
from flask import Flask, Response, request, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

from src import export

class Routing(object):
    app = Flask(__name__)
    file_name = ""
    connection = ""
        
    @app.route('/')
    def upload():
        return render_template("upload.html")

    @app.route('/plot.png')
    def plot_png():
        fig = Routing.connection.data['corr_heatmap']
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')


    @app.route('/describe', methods = ['POST'])
    def success():
        if request.method == 'POST':
            try:            
                Routing.file_name = request.files['file'].filename
                Routing.connection = export.Connect(Routing.file_name)
                Routing.connection.common_connector() 

                return render_template("describe.html", tables = Routing.connection.data['tables'],
                    info = Routing.connection.data['info'],
                    description =  Routing.connection.data['description'],
                )
                
            except Exception:
                return render_template("upload.html") #, error = 'Incorrect data format'
        else:
            return render_template("upload.html") #, error = 'File not provided'

    
# 
      # 
if __name__ == '__main__':
    Routing.app.run(debug = True)

# if __name__ == '__main__':
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
