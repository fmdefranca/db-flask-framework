from flask import Flask, render_template, flash, request
from flask_assets import Bundle, Environment

# database imports
import pyodbc

# create app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is my secret key'

# assets: https://flask-assets.readthedocs.io/en/latest/
assets = Environment(app)
assets.url = app.static_url_path

# JS Files
js = Bundle(
    "assets/node_modules/jquery/dist/jquery.min.js",
    "assets/node_modules/@popperjs/core/dist/umd/popper.min.js",
    "assets/node_modules/bootstrap/dist/js/bootstrap.min.js",
    "assets/main.js",
    #filters="jsmin",
    output="js/generated.js",
)
assets.register("js_all", js)

# SCSS files
scss = Bundle(
    "assets/main.scss",  # 1. Will read this scss file and generate a css file based on it
    filters="libsass",  # 2. Us this filter: https://webassets.readthedocs.io/en/latest/builtin_filters.html#libsass
    output="css/scss-generated.css",  # 3. And output the generated .css file to the static/css folder
)
assets.register(
    "scss_all", scss
)  # 4. Register the generated css file, to be used in Jinja template (see base.html)

# app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sfdc")
def sfdc():
    return render_template("sfdc.html")

@app.route("/supplypro", methods=['GET', 'POST'])
def supplyPro():
    
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=austin\\exelefacs;DATABASE=supplypro2;UID=supplypro2;PWD=sp2")
    cursor = conn.cursor()
    cursor.execute("show ''")
    fetchData = cursor.fetchall()
    if request.method == 'POST':
        if request.form['submit'] == 'searchBtn':
            cursor.execute(f"show '{request.form.get('partnumber')}'")
            fetchData = cursor.fetchall()
            return render_template("supplypro.html", fetchData=fetchData)
            conn.close()
        elif request.form['submit'] == 'takeBtn':
            print(f'take button pressed')
        elif request.form['submit'] == 'addBtn':
            print(f'add button pressed')
        # partNumber = request.form.get('partnumber')
        # idbadge = request.form.get('idbadge')
        # quantity = request.form.get('quantity')
    conn.close()
    return render_template("supplypro.html", fetchData=fetchData)
    #flash("this is a flashed message.", "success")

@app.route("/datamatrix", methods=['GET', 'POST'])
def dataMatrixChecker():
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=austin\\exelefacs;DATABASE=efacdb;UID=efacs;PWD=FSbtgDubu4A6")
    cursor = conn.cursor()
    if request.method == 'POST':
        if request.form['submit'] == 'validateBtn':
            cursor.execute(f"exec dbo.mo_laserQR '{request.form.get('fixtureQrCode')}'")
            fetchData = cursor.fetchall()
            print(fetchData)
            return render_template("datamatrix.html", fetchData=fetchData)

    return render_template("datamatrix.html")

if __name__ == "__main__":
    app.run(debug=True)