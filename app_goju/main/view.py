from flask import render_template,url_for,redirect
from app_goju.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')