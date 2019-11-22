from flask import *  
import pandas as pd
app = Flask(__name__)  
     
@app.route('/')  
def upload():  
    return render_template("upload.html")  
     
@app.route('/describe', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        # f.save(f.filename)
        return render_template("describe.html", name = pd.read_csv(f))  
      
if __name__ == '__main__':  
    app.run(debug = True)  