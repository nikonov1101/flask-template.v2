from flask import Blueprint, render_template

index = Blueprint('index', __name__, url_prefix='/')


@index.route('/', methods=['GET'])
def show_index():
    """ just render index page template """
    return render_template("index/index.html")
