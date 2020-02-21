from flask import Blueprint, render_template
from flask_login import login_required, current_user
from cious import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/cam')
@login_required
def cam():
    return render_template('cam.html', name=current_user.name)

