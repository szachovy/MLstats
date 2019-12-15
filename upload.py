#!/usr/bin/env python3


from flask import Flask, Response, request, render_template
from werkzeug import secure_filename

############ self defined
from src import export

########################
app = Flask(__name__) 

class Routing(object):
    '''
    Routing interface responsible for management between web pages
    and python modules.

    To use:
        open web browser:
            http://127.0.0.1:5000
    
    '''
    connection = ''
        
    @app.route('/')
    def upload():
        '''
        Interface responsible for inserting data file

        Possible extensions are:
            - .csv
            - .xlsx
            - .json

        Project hasn`t got embedded intelligence with recognizing dataframes inside file
        among several things.

        The best way to make sure that your file is appropiate is to send file with `pandas` dataframe object.
        Project base on pandas/numpy solutions.

        Interface is fault tolerant.
        '''
        return render_template("upload.html")

    @app.route('/describe', methods = ['POST'])
    def success():
        '''
        Interface which aims to render data set analysis.

        Provided file is sent to python modules,
        after calculations feedback is generated on the web page.

        Further versions will generalize file inserted, behaviour of the program may be unexpected.
        
        Depends on machine and data size, calculations will take some time.         
        '''
        
        if request.method == 'POST':

            # if file not provided, get back to index file
            if not request.files['file'].filename:
                return render_template("upload.html", error_info = 'Please insert file to analyse')
                
            Routing.file_name = request.files['file'].filename

            request.files['file'].save(secure_filename(request.files['file'].filename))
            Routing.connection = export.Connect(Routing.file_name)

            return render_template("describe.html", common = Routing.connection.common_connector(),
                        single = Routing.connection.single_connector(),
                        mixed = Routing.connection.mixed_connector(),
                        plots = Routing.connection.plot_url_list()
                        )
                  
if __name__ == '__main__':
    app.run(debug = True)
