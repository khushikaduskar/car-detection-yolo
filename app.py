from flask import Flask, render_template, request
import os
from yolo.detect import detect_image

app = Flask(__name__)

# Create upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    image_path = ""

    if request.method == 'POST':
        file = request.files['file']

        if file and file.filename != "":
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            result = detect_image(filepath)
            image_path = filepath

    return render_template('index.html', result=result, image=image_path)

if __name__ == '__main__':
    app.run(debug=True, port=5001)