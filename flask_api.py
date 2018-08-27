import os
import numpy as np
import cv2
from flask import Flask, flash, request, redirect, url_for,json,Response
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import io
import datetime
import time


app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

		   
def process_image(image):
    #pass image to model and receive the output and return it via response object
	#temp values
	return {
        'desease':['a','b'],
        'remedy':['c','d']
    }
    
@app.route('/uploadImage/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return Response('No file uploaded', status=500)

            
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            ts=time.time()
            save_as = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')
            save_as=save_as+'.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], save_as))
            image=cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], save_as))
            data=process_image(image)            
            return  Response(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
        
        return Response('Invalid format', status=422)
        
if __name__ == '__main__':
    app.run()