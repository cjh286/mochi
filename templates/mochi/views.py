from flask import render_template, Blueprint
mochi_blueprint = Blueprint('mochi',__name__)
@mochi_blueprint.route('/')
@mochi_blueprint.route('/mochi')
def index():
    return render_template("index.html")