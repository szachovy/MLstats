
__author__ = 'WJ Maj'

from flask import Flask, Response, request, render_template
from werkzeug import secure_filename
from src import export

app = Flask(__name__) 

class Routing(object):
    connection = ''
        
    @app.route('/')
    def upload():
        return render_template("upload.html")

    @app.route('/describe', methods = ['POST'])
    def success():
        if request.method == 'POST':
            request.files['file'].save(secure_filename(request.files['file'].filename))
            Routing.file_name = request.files['file'].filename
            
            Routing.connection = export.Connect(Routing.file_name)

            return render_template("describe.html", common = Routing.connection.common_connector(),
                        single = Routing.connection.single_connector(),
                        mixed = Routing.connection.mixed_connector(),
                        plots = Routing.connection.plot_url_list()
                        )
    
        else:
            return render_template("upload.html") #, error = 'File not provided'
                  
if __name__ == '__main__':
    app.run(debug = True)