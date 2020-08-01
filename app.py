#Add flask packages
from flask import Flask, render_template, redirect, request, jsonify, url_for
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
import os

# ******************************************************** 
# Configuration part
# ********************************************************

#Initialize the flask app
app = Flask(__name__)

#Configure the upload folder for storing pdfs
UPLOAD_FOLDER = './books'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#Configure the MySQL database
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'db password'
app.config['MYSQL_DATABASE_DB'] = 'OurLibrary'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

#Check if DB is connected or not
if cursor: 
    print("Congrats!! Database is connected!!")
else:
    print("Oops!! Database is not connected!!")



# ****************************************
# Routes to admin panel
# ****************************************

#Route for admin dashboard
@app.route('/admin/dashboard', methods = ["GET"])
def admin():
    if request.method == "GET":
        return render_template('/adminPanel/admin.html')


#Route for saving any admin uploaded pdf
@app.route('/admin/save_pdf', methods = ["POST", "GET"])
def admin_save():
    if request.method == "POST":
        userData = request.form
        file = request.files['file']
        print(userData)
        
        #If there is any file
        if file:
            for f in request.files.getlist('file'):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        stat = "Done..."
        return redirect(url_for('done', stat = stat))
    elif request.method == "GET":
        return render_template('/adminPanel/error.html')



# *****************************************
# Default Routes
# *****************************************

#Route for testing done
@app.route('/done')
def done():
    # if request.method == "GET":
    return render_template('/adminPanel/extra.html', success = request.args.get("stat"))

#Route for testing purpose
@app.route('/test',methods=["POST","GET"])
def testing():
    return render_template('/adminPanel/error.html')

@app.route('/signup',methods=["POST","GET"])
def registration():
    return render_template('/Admin_Pannel/signup.html')
            
if __name__ == "__main__":
    app.run(debug = True)
