from flask import Flask, render_template, redirect, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './books'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return "Bye"


@app.route('/Admin', methods = ["GET"])
def admin():
    if request.method == "GET":
        return render_template('/Admin_Pannel/Admin.html')

@app.route('/done')
def done():
    # if request.method == "GET":
    return render_template('/Admin_Pannel/extra.html', success = request.args.get("stat"))


@app.route('/admin_save', methods = ["POST", "GET"])
def admin_save():
    if request.method == "POST":
        print("Hello")
        userData = request.form
        file = request.files['file']
        
        print(userData)
        if file:
            print(file)
            # filename = secure_filename(file.filename)

            for f in request.files.getlist('file'):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        stat = "Done..."
        return redirect(url_for('done', stat = stat))



@app.route('/test',methods=["POST","GET"])
def testing():
    return render_template('/Admin_Pannel/error.html')
            
if __name__ == "__main__":
    app.run(debug = True)
