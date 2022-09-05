from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import dataexplorer 
import os 
import pathlib 
app = Flask(__name__)

# Temp storage
UPLOAD_FOLDER = os.getcwd() + '/temp/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/uploader', methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print("File Saved!")
      result = dataexplorer.main(filename)
      return jsonify(result)

def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
    

if __name__ == '__main__':
   pathlib.Path(os.getcwd() + '/temp/').mkdir(parents=True, exist_ok=True)
   app.run(host='localhost', port=3001, debug=True)
