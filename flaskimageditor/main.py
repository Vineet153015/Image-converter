from flask import Flask, render_template , request ,flash
from werkzeug.utils import secure_filename
import os
import cv2 

UPLOAD_FOLDER = "flaskimageditor\\uploads"
ALLOWED_EXTENSIONS = { 'webp', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(filename,operation):
    print(f"The operation is {operation} and the file is {filename}")
    pick=cv2.imread(f"flaskimageditor\\uploads\{filename}")
    match operation:
        case "cgray":
            process = cv2.cvtColor( pick , cv2.COLOR_BGR2GRAY)
            newFilename=f"flaskimageditor\\static\ {filename}"
            cv2.imwrite(newFilename,process)
            return newFilename
        case "cwebp":
            newFilename=f"flaskimageditor\\static\ {filename.split('.')[0]}.webp"
            cv2.imwrite(newFilename,pick)
            return newFilename
        case "cjpg":
            newFilename=f"flaskimageditor\\static\ {filename.split('.')[0]}.jpg"
            cv2.imwrite(newFilename,pick)
            return newFilename
        case "cpng":
            newFilename=f"flaskimageditor\\static\ {filename.split('.')[0]}.png"
            cv2.imwrite(newFilename,pick)
            return newFilename
    pass

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/howtouse")
def use():
    return render_template("howtouse.html")

@app.route("/contactus")
def contact():
    return render_template("contactus.html")


@app.route("/edit",methods =["GET","POST"])
def edit():
    if request.method == "POST":
        operation = request.form.get("operation")
    # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "ERROR"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "No Selected file"
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new=processImage(filename , operation)
            flash(f"Your Image is processed and is available<a href='#flaskimageditor\static\{new}' target='_blank'>Here</a>")
            return render_template("index.html")
    return render_template("index.html")



app.run(debug=True)