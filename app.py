from flask import Flask, render_template
from flask_assets import Bundle, Environment

# create app
app = Flask(__name__)

# assets: https://flask-assets.readthedocs.io/en/latest/
assets = Environment(app)
assets.url = app.static_url_path

# JS Files
js = Bundle(
    "assets/node_modules/jquery/dist/jquery.min.js",
    "assets/node_modules/@popperjs/core/dist/umd/popper.min.js",
    "assets/node_modules/bootstrap/dist/js/bootstrap.min.js",
    filters="jsmin",
    output="js/generated.js"
)
assets.register("js_all", js)

# SCSS files
scss = Bundle(
    "assets/main.scss", # 1. Will read this scss file and generate a css file based on it
    filters="libsass",  # 2. Us this filter: https://webassets.readthedocs.io/en/latest/builtin_filters.html#libsass
    output="css/scss-generated.scss" # 3. And output the generated .css file to the static/css folder
)
assets.register("scss_all", scss) # 4. Register the generated css file, to be used in Jinja template (see base.html)

# app routes
@app.route("/")
def index():
    return render_template("index.html")
