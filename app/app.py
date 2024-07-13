from flask import Flask, render_template, request, redirect, url_for, flash
import os
import tensorflow as tf
import keras
import numpy as np
import cv2 as cv
from keras.models import model_from_json

# Load your model
with open("model/model_architecture_Xception.json", "r") as json_file:
    loaded_model_json = json_file.read()
    loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("model/model_Xception.h5")



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'supersecretkey'

animals = {
    0: "Black Panther",
    1: "Cat",
    2: "Cheetah",
    3: "Jaguar",
    4: "Leopard",
    5: "Lion",
    6: "Puma",
    7: "Tiger"
}


def predict_image(image_path):
    try:
        # Load the image
        image = cv.imread(image_path)  # Adjust target size according to your model
        image = cv.resize(image, (180, 180))
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = image / 255
        image = np.array([image])
        prediction = loaded_model.predict(image)
        return np.argmax(prediction)
    except Exception as e:
        return str(e)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return redirect(url_for('prediction', filename=file.filename))
    return render_template('upload.html')


@app.route('/prediction/<filename>')
def prediction(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    result = predict_image(filepath)
    if isinstance(result, str):
        flash(result)
        return redirect(url_for('upload'))
    return render_template('prediction.html', filename=filename, result=animals[result])


if __name__ == '__main__':
    app.run(debug=True)

