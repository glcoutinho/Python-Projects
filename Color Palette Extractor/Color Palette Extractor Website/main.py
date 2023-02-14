import os
from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from color_extration import path_to_img_array, pick_colors, show_key_colors

UPLOAD_FOLDER = 'static\images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Bootstrap(app)
app.secret_key = 'fuckideletehis'


@app.route("/")
def home():
    hide = True
    return render_template("index.html", hide=hide)


@app.route('/', methods=("POST", "GET"))  # methods
def uploadFile():
    if request.method == 'POST':  # request
        # Upload file flask
        uploaded_img = request.files['uploaded-file']  # o q recebeu para folder
        # Extracting uploaded data file name
        img_filename = secure_filename(uploaded_img.filename)  # werkzeug.utils
        # Upload file to database (defined uploaded folder in static path)
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))  # complicaded upload ?
        # Storing uploaded file path in flask session
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)  # import
        # session ?
        img_file_path = session.get('uploaded_img_file_path', None)  # Retrieving uploaded file path from session
        # EXTRATION
        # Load an image up to a vector, from a given path
        path = f'static/images/{img_filename}'
        vec = path_to_img_array(path)

        # Unrolls our image and runs K-Means clustering to find "Target Points" all of the pixel values are grouped around
        color_value = request.form.get("nrcolors")
        print(color_value)

        colors = pick_colors(vec, int(color_value))
        rgb = str(show_key_colors(colors)).replace("[", "").replace("]", "")
        palete_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'savethis.png')  # Display in html
        print(rgb)

        return render_template('index.html', user_image=img_file_path, user_image_palete=palete_filename, RGB=rgb)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
