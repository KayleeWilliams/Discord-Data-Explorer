from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import os
import pathlib
from main import main

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
      # Return results or error
      try: 
         return jsonify(main(filename))
      except Exception as e:
         return jsonify({'error': str(e)}), 400


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
   pathlib.Path(os.getcwd() + '/temp/').mkdir(parents=True, exist_ok=True)
   app.run(host='0.0.0.0', port=3003, debug=True)
   # Run app on http://192.168.1.229:3001
