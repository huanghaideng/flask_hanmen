from flask import Blueprint

bp = Blueprint('gojudaquan',__name__)

from app_goju.gojudaquan import goju_view