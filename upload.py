from flask import *  
import pandas as pd

from src import common
from src import individual

# app = Flask(__name__)
     # 
# @app.route('/')
# def upload():
    # return render_template("upload.html")
     # 
# @app.route('/describe', methods = ['POST'])
# def success():
    # if request.method == 'POST':
        # f = request.files['file']
        # f.save(f.filename)
        # return render_template("describe.html", name = pd.read_csv(f))
      # 
# if __name__ == '__main__':
    # app.run(debug = True)

if __name__ == '__main__':
    # common.Extract.check_input('sample2.csv')
    mutual = common.Mutual_description('train.csv')
    # print(mutual.show_table())
    # print(mutual.data_info())
    # print(mutual.data_description())
    # mutual.correlations_heatmap()

    singular = individual.Singular_description('train.csv')
    singular.histogram()
    # print(singular.average())
    # print(singular.expected_value())
    # print(singular.median())
    # print(singular.mode())