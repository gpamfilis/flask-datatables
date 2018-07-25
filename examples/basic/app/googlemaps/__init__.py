from flask import Blueprint

gmaps = Blueprint('gmaps', __name__, template_folder='templates/')

from . import views
