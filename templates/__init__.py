from flask import Flask
app = Flask(__name__,
    static_folder = './public',
    template_folder="./static")
from templates.mochi.views import mochi_blueprint
# register the blueprints
app.register_blueprint(mochi_blueprint)