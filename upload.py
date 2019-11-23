from flask import *  
import pandas as pd

from src import common

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
    general = common.Mutual_description('train.csv')
    print(general.show_table())
    print(general.data_info())
    print(general.data_description())
    general.correlations_heatmap()